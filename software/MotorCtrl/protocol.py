import struct

class CANMsg(struct.Struct):
    ID_STD = 0
    ID_EXT = 4
    RTR_DATA = 0
    RTR_REMOTE = 2

    TAG_RX_MSG = 0x11
    TAG_TX_MSG = 0x12

    # Version 1.0
    # P_MIN = -95.5
    # P_MAX = 95.5
    # V_MIN = -45.0
    # V_MAX = 45.0
    # KP_MIN = 0.0
    # KP_MAX = 500.0
    # KD_MIN = 0.0
    # KD_MAX = 5.0
    # I_MIN = -18.0
    # I_MAX = 18.0

    # Version 2.0
    P_MIN = -12.5
    P_MAX = 12.5
    V_MIN = -65.0
    V_MAX = 65.0
    KP_MIN = 0.0
    KP_MAX = 500.0
    KD_MIN = 0.0
    KD_MAX = 5.0
    I_MIN = -40.0
    I_MAX = 40.0

    def __init__(self, format) -> None:
        super().__init__(format)

        self.data = bytearray(8)

    def float_to_uint(x, x_min, x_max, bits):
        span = x_max - x_min
        offset = x_min
        return int((x - offset) * ((1 << bits) - 1) / span)

    def uint_to_float(x, x_min, x_max, bits):
        span = x_max - x_min
        offset = x_min
        return (float(x) * span / float((1 << bits) - 1)) + offset


class CANTxMsg(CANMsg):

    MOTOR_CMD = 0xFC
    MENU_CMD = 0xFD
    ZERO_CMD = 0xFE

    MAGIC = 0xa55a

    def __init__(self) -> None:
        super().__init__('=HBBIBBHBBBBBBBBI')

        self.magic = CANTxMsg.MAGIC
        self.tag = CANMsg.TAG_TX_MSG
        self.length = self.size - 4 # Not include CRC32 sum
        self.padding = 0
        self.checksum = 0

        self.ID = 0
        self.IDE = CANMsg.ID_STD
        self.DLC = 0

        # float
        self.position = 0
        self.velocity = 0
        self.kp = 0
        self.kd = 0
        self.torque = 0 # I * KT * GR

        # uint
        self._position = 0
        self._velocity = 0
        self._kp = 0
        self._kd = 0
        self._torque = 0

    def pack(self) -> bytes:

        # CAN Command Packet Structure
        # 16 bit position command, between -4*pi and 4*pi
        # 12 bit velocity command, between -30 and + 30 rad/s
        # 12 bit kp, between 0 and 500 N-m/rad
        # 12 bit kd, between 0 and 100 N-m*s/rad
        # 12 bit feed forward torque, between -18 and 18 N-m
        # CAN Packet is 8 8-bit words
        # Formatted as follows.  For each quantity, bit 0 is LSB
        # 0: [position[15-8]]
        # 1: [position[7-0]]
        # 2: [velocity[11-4]]
        # 3: [velocity[3-0], kp[11-8]]
        # 4: [kp[7-0]]
        # 5: [kd[11-4]]
        # 6: [kd[3-0], torque[11-8]]
        # 7: [torque[7-0]]

        self._position = CANMsg.float_to_uint(self.position, CANMsg.P_MIN, CANMsg.P_MAX, 16)
        self._velocity = CANMsg.float_to_uint(self.velocity, CANMsg.V_MIN, CANMsg.V_MAX, 12)
        self._kp = CANMsg.float_to_uint(self.kp, CANMsg.KP_MIN, CANMsg.KP_MAX, 12)
        self._kd = CANMsg.float_to_uint(self.kd, CANMsg.KD_MIN, CANMsg.KD_MAX, 12)
        self._torque = CANMsg.float_to_uint(self.torque, CANMsg.I_MIN, CANMsg.I_MAX, 12)

        # print("{} {} {} {} {}".format(self._position, self._velocity, self._kp, self._kd, self._torque))

        self.data[0] = (self._position >> 8) & 0xFF
        self.data[1] = self._position & 0xFF
        self.data[2] = (self._velocity >> 4) & 0xFF
        self.data[3] = ((self._velocity << 4) & 0xF0) | ((self._kp >> 8) & 0x0F)
        self.data[4] = self._kp & 0xFF
        self.data[5] = (self._kd >> 4) & 0xFF
        self.data[6] = ((self._kd << 4) & 0xF0) | ((self._torque >> 8) & 0x0F)
        self.data[7] =  self._torque & 0xFF

        return super().pack(self.magic, self.tag, self.length, \
                self.ID, self.IDE, self.DLC, self.padding, \
                self.data[0], self.data[1], self.data[2], self.data[3], \
                self.data[4], self.data[5], self.data[6], self.data[7], self.checksum)

    def pack_cmd(self, cmd) -> bytes:
        return super().pack(self.magic, self.tag, self.length, \
                self.ID, self.IDE, self.DLC, self.padding, \
                0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, cmd, self.checksum)


class CANRxMsg(CANMsg):

    MAGIC = 0x5aa5

    def __init__(self) -> None:
        super().__init__('=HBBIBBHBBBBBBBBI')

        self.magic = 0
        self.tag = 0
        self.length = 0
        self.padding = 0
        self.checksum = 0

        self.ID = 0
        self.IDE = CANMsg.ID_STD
        self.DLC = 0

        # float
        self.id = 0
        self.position = 0
        self.velocity = 0
        self.torque = 0 # I * KT * GR

        # uint
        self._position = 0
        self._velocity = 0
        self._torque = 0
    
    def unpack(self, buf) -> None:

        # CAN Reply Packet Structure
        # 16 bit position, between -4*pi and 4*pi
        # 12 bit velocity, between -30 and + 30 rad/s
        # 12 bit current, between -40 and 40;
        # CAN Packet is 5 8-bit words
        # Formatted as follows.  For each quantity, bit 0 is LSB
        # 0: [id]
        # 1: [position[15-8]]
        # 2: [position[7-0]]
        # 3: [velocity[11-4]]
        # 4: [velocity[3-0], current[11-8]]
        # 5: [current[7-0]]

        self.magic, self.tag, self.length, \
                self.ID, self.IDE, self.DLC, self.padding, \
                self.data[0], self.data[1], self.data[2], self.data[3], \
                self.data[4], self.data[5], self.data[6], self.data[7], \
                self.checksum = super().unpack(buf)

        self._position = ((self.data[1] << 8) & 0xFF00) | (self.data[2] & 0xFF)
        self._velocity = ((self.data[3] << 4) & 0x0FF0) | ((self.data[4] >> 4) & 0x0F)
        self._torque = ((self.data[4] << 8) & 0x0F00) | (self.data[5] & 0xFF)

        self.id = self.data[0]
        self.position = CANMsg.uint_to_float(self._position, CANMsg.P_MIN, CANMsg.P_MAX, 16)
        self.velocity = CANMsg.uint_to_float(self._velocity, CANMsg.V_MIN, CANMsg.V_MAX, 12)
        self.torque = CANMsg.uint_to_float(self._torque, CANMsg.I_MIN, CANMsg.I_MAX, 12)
