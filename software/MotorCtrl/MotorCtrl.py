import sys, serial, threading
from time import sleep
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt, Slot, QTime, QTimer
from PySide6.QtGui import QValidator
from motorpanel import Ui_MotorPanel
from valuesidler import Ui_ValueSidler
from protocol import CANMsg, CANRxMsg, CANTxMsg
from serial.tools import list_ports

class ValueSidler(QtWidgets.QWidget):
    def __init__(self, label, min, max, onValueChange = None) -> None:
        super().__init__()
        self.ui = Ui_ValueSidler()
        self.ui.setupUi(self)

        self.label = label
        self.min = min
        self.max = max
        self.defualt = 0
        self.onValueChange = onValueChange

        self.step = (max - min) / 100

        # print('max:{:+6.1f} min:{:+6.1f} step:{:+6.1f}'.format(
        #     self.max, self.min, self.step))

        self.fmt = '{:+1.1f}'
        if (self.step >= 1):
            self.fmt = '{:+1.0f}'
        elif (self.step < 0.1):
            self.fmt = '{:+1.2f}'

        self.ui.label.setText(label)
        self.ui.min.setText(self.fmt.format(self.min))
        self.ui.max.setText(self.fmt.format(self.max))

        self.ui.slider.setMinimum(int(self.min * 10))
        self.ui.slider.setMaximum(int(self.max * 10))
        self.ui.slider.setSingleStep(int(self.step * 10))
        self.ui.slider.setPageStep(int(self.step * 10))
        self.ui.slider.valueChanged.connect(self.sliderChange)

        if (self.step >= 1):
            self.ui.spin.setDecimals(0)
        elif (self.step < 0.1):
            self.ui.spin.setDecimals(2)
        self.ui.spin.setMinimum(self.min)
        self.ui.spin.setMaximum(self.max)
        self.ui.spin.setSingleStep(self.step)
        self.ui.spin.valueChanged.connect(self.spinChange)

        self.setValue(self.defualt)

    @Slot(int)
    def sliderChange(self, value):
        self.value = float(value) / 10.0
        self.ui.spin.setValue(self.value)
        if self.onValueChange != None:
            self.onValueChange(self.value)
        # print('{}: {}'.format(self.label, self.value))

    @Slot(float)
    def spinChange(self, value):
        self.value = value
        self.ui.slider.setValue(int(self.value * 10))
        if self.onValueChange != None:
            self.onValueChange(self.value)
        # print('{}: {}'.format(self.label, self.value))

    def setValue(self, value: float):
        self.value = value
        self.ui.spin.setValue(self.value)
        self.ui.slider.setValue(int(self.value * 10))

    def getValue(self) -> float:
        return self.value

    def reset(self):
        self.setValue(self.defualt)

class PeridValidator(QtGui.QValidator):
    def __init__(self, min, max):
        super().__init__()

        self.min = min
        self.max = max

    def validate(self, input: str, length: int):
        if len(input) == 0:
            return QValidator.Intermediate
        elif not input.isnumeric():
            return QValidator.Invalid

        v = int(input)
        if v < self.min or v > self.max:
            return QValidator.Intermediate

        if input.startswith('0'):
            return QValidator.Intermediate

        return QValidator.Acceptable

    def fixup(self, input: str):
        v = 0
        try:
            v = int(input)
        except:
            pass
        if v < self.min:
            v = self.min
        elif v > self.max:
            v = self.max
        return str(v)

class CANIDValidator(QtGui.QValidator):
    def __init__(self):
        super().__init__()

    def validate(self, input: str, length: int) -> object:
        # CANID: 0x0000 - 0x07FF
        # Adapter CANID: 0x0000
        v = 1
        try:
            if len(input) == 0:
                return QValidator.Intermediate
            if len(input) == 2 and input[1] == 'x':
                return QValidator.Intermediate
            elif input.startswith('0x'):
                v = int(input, base=16)
            elif input.isnumeric():
                v = int(input)
            else:
                return QValidator.Invalid
        except:
            return QValidator.Invalid
        
        if v < 0 or v > 0x07FF:
            return QValidator.Intermediate

        if not input.startswith('0x'):
            return QValidator.Intermediate
        
        # print('{} :{} :{}'.format(input, length, v))

        return QValidator.Acceptable

    def fixup(self, input: str):
        # print(input)
        v = 0
        try:
            if input.startswith('0x'):
                v = int(input, base=16)
            elif input.isnumeric():
                v = int(input)
        except:
            pass

        if v < 1:
            v = 1
        elif v > 0x07FF:
            v = 0x07FF
        return '0x{:02X}'.format(v)

class MotorPanel(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MotorPanel()
        self.ui.setupUi(self)

        self.rxMsg = CANRxMsg()
        self.txMsg = CANTxMsg()

        self.rxPosition = ValueSidler('Position', CANMsg.P_MIN, CANMsg.P_MAX)
        self.rxVelocity = ValueSidler('Velocity', CANMsg.V_MIN, CANMsg.V_MAX)
        self.rxTorque = ValueSidler('Torque', CANMsg.I_MIN, CANMsg.I_MAX)

        self.ui.rxGroupLayout.addWidget(self.rxPosition)
        self.ui.rxGroupLayout.addWidget(self.rxVelocity)
        self.ui.rxGroupLayout.addWidget(self.rxTorque)

        self.txPosition = ValueSidler('Position', CANMsg.P_MIN, CANMsg.P_MAX, self.onPositionChange)
        self.txVelocity = ValueSidler('Velocity', CANMsg.V_MIN, CANMsg.V_MAX, self.onVelocityChange)
        self.txKp = ValueSidler('Kp', CANMsg.KP_MIN, CANMsg.KP_MAX, self.onKpChange)
        self.txKd = ValueSidler('Kd', CANMsg.KD_MIN, CANMsg.KD_MAX, self.onKdChange)
        self.txTorque = ValueSidler('Torque', CANMsg.I_MIN, CANMsg.I_MAX, self.onTorqueChange)

        self.ui.txGroupLayout.addWidget(self.txPosition)
        self.ui.txGroupLayout.addWidget(self.txVelocity)
        self.ui.txGroupLayout.addWidget(self.txKp)
        self.ui.txGroupLayout.addWidget(self.txKd)
        self.ui.txGroupLayout.addWidget(self.txTorque)

        self.ui.startButton.toggled.connect(self.startToggled)

        self.ui.idEntry.setValidator(CANIDValidator())
        self.ui.peridEntry.setValidator(PeridValidator(2, 1000))

        self.ui.protBox.clear()
        self.ports = list_ports.comports()
        self.foundport = False
        
        for i, port in enumerate(self.ports):
            self.ui.protBox.insertItem(i, '{} [{}]'.format(port.product, port.device))
            # prefer items contain CAN
            if port.product is not None and 'can' in port.product.lower():
                self.ui.protBox.setCurrentIndex(i)
                self.foundport = True
            else:
                self.ui.protBox.model().item(i).setEnabled(False)

            # print('{}:{}:{}:{}:{}:{}:{}'.format(i, port.device, port.name,
            #       port.description, port.serial_number, port.manufacturer, port.product))
        
        if (self.foundport):        
            self.ui.startButton.setEnabled(True)
            self.ui.protBox.setEnabled(True)
        else:
            self.ui.startButton.setEnabled(False)
            self.ui.protBox.setEnabled(False)

        self.timer_dt = 100
        self.timer_ms = 0
        self.timer = QTimer()
        self.timer.setInterval(self.timer_dt)
        self.timer.timeout.connect(self.onUpdateRxMessage)

        self.dt = 1
        self.start = threading.Event()
        self.fault = threading.Event()

        self.rxError = 0
        self.rxCount = 0
        self.txCount = 0

        self.time = QTime()

    def onPositionChange(self, value):
        self.txMsg.position = value

    def onVelocityChange(self, value):
        self.txMsg.velocity = value

    def onKpChange(self, value):
        self.txMsg.kp = value

    def onKdChange(self, value):
        self.txMsg.kd = value

    def onTorqueChange(self, value):
        self.txMsg.torque = value

    def onUpdateRxMessage(self):
        self.timer_ms += self.timer_dt
        self.rxPosition.setValue(self.rxMsg.position)
        self.rxVelocity.setValue(self.rxMsg.velocity)
        self.rxTorque.setValue(self.rxMsg.torque)
        self.ui.status_rx.setText(str(self.rxCount))
        self.ui.status_tx.setText(str(self.txCount))
        self.ui.status_error.setText(str(self.rxError))
        self.ui.status_dt.setText(str(self.dt))
        self.time = self.time.addMSecs(self.timer_dt)
        self.ui.status_time.setText(str(self.time.toString(f=Qt.DateFormat.ISODateWithMs)))

        if self.fault.is_set():
            self.ui.status_status.setText('Fault')
            self.ui.startButton.setText('Reset')

    def setControlEnabled(self, enable):
        self.ui.idEntry.setEnabled(enable)
        self.ui.peridEntry.setEnabled(enable)
        self.ui.protBox.setEnabled(enable)

        self.rxPosition.reset()
        self.rxVelocity.reset()
        self.rxTorque.reset()

        self.txPosition.reset()
        self.txVelocity.reset()
        self.txKp.reset()
        self.txKd.reset()
        self.txTorque.reset()

        if enable == True:
            self.ui.status_status.setText('Idle')
        else:
            self.ui.status_status.setText('Running')

    def rxThreadProc(self):
        timeout = 0
        while(self.start.is_set()):
            buf = self.serial.read(24)
            # check buffer magic/checksum
            if len(buf) == 0:
                timeout += self.serial.timeout
            elif len(buf) >= 24:
                self.rxMsg.unpack(buf)
                self.rxCount += 1
                timeout = 0
            else:
                self.rxError += 1

            if timeout > 0.5 or self.rxError > 10:
                self.start.clear()
                self.fault.set()

    def txThreadProc(self):
        msg = CANTxMsg()
        msg.ID = self.canId
        msg.DLC = 0x08

        self.txMsg.ID = self.canId
        self.txMsg.DLC = 0x08

        # Set current positon as zero position
        # self.serial.write(msg.pack_cmd(CANTxMsg.ZERO_CMD))

        # Enter Motor Mode
        self.serial.write(msg.pack_cmd(CANTxMsg.MOTOR_CMD))

        while(self.start.is_set()):
            sleep(self.dt)
            self.serial.write(self.txMsg.pack())
            self.txCount += 1

        # Exit Motor Mode
        self.serial.write(msg.pack_cmd(CANTxMsg.MENU_CMD))

    def startLoop(self):
        i = self.ui.protBox.currentIndex()
        self.perid = float(self.ui.peridEntry.text())
        self.dt = 1.0 / self.perid
        self.canId = int(self.ui.idEntry.text(), base=16)
        # print(self.ports[i])
        # print(self.dt)

        self.serial = serial.Serial(self.ports[i].device)
        self.serial.timeout = self.dt * 100

        self.time.setHMS(0, 0, 0)
        self.timer_ms = 0
        self.timer.start()

        self.start.set()
        self.fault.clear()

        self.rxThread = threading.Thread(target=self.rxThreadProc)
        self.rxThread.daemon = True
        self.rxThread.start()

        self.txThread = threading.Thread(target=self.txThreadProc)
        self.txThread.daemon = True
        self.txThread.start()

    def stopLoop(self):
        
        self.start.clear()
        self.fault.clear()
        
        self.rxCount = 0
        self.txCount = 0
        self.rxError = 0

        self.txThread.join()
        self.rxThread.join()

        self.timer.stop()
        self.serial.close()

    @Slot(bool)
    def startToggled(self, toggled):
        if toggled == True:
            self.ui.startButton.setText('Stop')
            self.setControlEnabled(False)
            self.startLoop()
        else:
            self.ui.startButton.setText('Start')
            self.setControlEnabled(True)
            self.stopLoop()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    panel = MotorPanel()
    panel.show()
    app.exec()