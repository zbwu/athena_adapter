/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : usbd_cdc_if.h
  * @version        : v1.0_Cube
  * @brief          : Header for usbd_cdc_if.c file.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2022 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __USBD_CDC_IF_H__
#define __USBD_CDC_IF_H__

#ifdef __cplusplus
 extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "usbd_cdc.h"

/* USER CODE BEGIN INCLUDE */

/* USER CODE END INCLUDE */

/** @addtogroup STM32_USB_OTG_DEVICE_LIBRARY
  * @brief For Usb device.
  * @{
  */

/** @defgroup USBD_CDC_IF USBD_CDC_IF
  * @brief Usb VCP device module
  * @{
  */

/** @defgroup USBD_CDC_IF_Exported_Defines USBD_CDC_IF_Exported_Defines
  * @brief Defines.
  * @{
  */
/* Define size for the receive and transmit buffer over CDC */
#define APP_RX_DATA_SIZE  2048
#define APP_TX_DATA_SIZE  2048
/* USER CODE BEGIN EXPORTED_DEFINES */
#define TAG_MSG     0x01
#define TAG_ERROR   0x02
#define TAG_RX_MSG  0x11
#define TAG_TX_MSG  0x12
/* USER CODE END EXPORTED_DEFINES */

/**
  * @}
  */

/** @defgroup USBD_CDC_IF_Exported_Types USBD_CDC_IF_Exported_Types
  * @brief Types.
  * @{
  */

/* USER CODE BEGIN EXPORTED_TYPES */
typedef struct
{
  uint16_t magic; // 5A A5
  uint8_t tag;
  uint8_t length;
} __attribute__((packed)) HubHeaderTypeDef;

typedef struct
{
  HubHeaderTypeDef header;
  uint16_t status;
  uint16_t buffer[8];
} __attribute__((packed)) HubStatusTypeDef;

typedef struct
{
  HubHeaderTypeDef header;
  uint32_t id;
  uint8_t ide;
  uint8_t dlc;
  uint8_t padding[2];
  uint8_t data[8];
} __attribute__((packed)) HubTxMsgTypeDef;

typedef struct
{
  HubHeaderTypeDef header;
  uint32_t id;
  uint8_t ide;
  uint8_t dlc;
  uint8_t padding[2];
  uint8_t data[8];
} __attribute__((packed)) HubRxMsgTypeDef;

/* USER CODE END EXPORTED_TYPES */

/**
  * @}
  */

/** @defgroup USBD_CDC_IF_Exported_Macros USBD_CDC_IF_Exported_Macros
  * @brief Aliases.
  * @{
  */

/* USER CODE BEGIN EXPORTED_MACRO */

/* USER CODE END EXPORTED_MACRO */

/**
  * @}
  */

/** @defgroup USBD_CDC_IF_Exported_Variables USBD_CDC_IF_Exported_Variables
  * @brief Public variables.
  * @{
  */

/** CDC Interface callback. */
extern USBD_CDC_ItfTypeDef USBD_Interface_fops_HS;

/* USER CODE BEGIN EXPORTED_VARIABLES */
extern CAN_TxHeaderTypeDef txMsgHeader;
extern CAN_RxHeaderTypeDef rxMsgHeader;
extern HubTxMsgTypeDef sHubTxMsg;
extern HubRxMsgTypeDef sHubRxMsg;
/* USER CODE END EXPORTED_VARIABLES */

/**
  * @}
  */

/** @defgroup USBD_CDC_IF_Exported_FunctionsPrototype USBD_CDC_IF_Exported_FunctionsPrototype
  * @brief Public functions declaration.
  * @{
  */

uint8_t CDC_Transmit_HS(uint8_t* Buf, uint16_t Len);

/* USER CODE BEGIN EXPORTED_FUNCTIONS */

/* USER CODE END EXPORTED_FUNCTIONS */

/**
  * @}
  */

/**
  * @}
  */

/**
  * @}
  */

#ifdef __cplusplus
}
#endif

#endif /* __USBD_CDC_IF_H__ */

