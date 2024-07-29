#в этом файле все константы
magic_word = 'BIKEMI_LL_START_PROGRAMMING'
password_to_change_serial = 'KEBI ADMIN'
size_setttings_buf = 102

#номера команд от ПК
COMMAND_CONNECTION = 0x19
COMMAND_READ_ALL_SETTINGS = 0x28
COMMAND_WRITE_WORK_SETTINGS = 0x37
COMMAND_WRITE_UART_SETTINGS = 0x37
COMMAND_WRITE_SERIAL_NUMBER = 0x55
COMMAND_RESET_MCU = 0x91

COMMAND_CONNECTION_NEG = 0xE6
COMMAND_READ_ALL_SETTINGS_NEG = 0xD7
COMMAND_WRITE_WORK_SETTINGS_NEG = 0xC8
COMMAND_WRITE_UART_SETTINGS_NEG = 0xC8
COMMAND_WRITE_SERIAL_NUMBER_NEG = 0xAA
COMMAND_RESET_MCU_NEG = 0x6E

#индексы буфера
INDEX_COMMAND = 0
INDEX_COMMAND_NEG = 1
INDEX_SERIALNUMBER_H = 2
INDEX_SERIALNUMBER_L = 3

#возможные скорости юарта
SPEED_LIST = [9600, 19200, 38600, 4800, 2400]
PARITY_LIST = ['N', 'E', 'O']
STOPBITS_LIST = [1, 1.5, 2]

#settings_default
DEFAULT_CONTROL_SOURCE = 0   #источник управления 0-входы, 1-модбас, 2-смешанный
DEFAULT_A1 = 1
DEFAULT_B1 = 0
DEFAULT_A2 = 1
DEFAULT_B2 = 0
DEFAULT_A3 = 1
DEFAULT_B3 = 0
DEFAULT_CONVERT_COUNT = 10	        #количество измерений ацп
DEFAULT_PASS_CONVERT_COUNT = 2		#количество первых пропускаемых измерений ацп
DEFAULT_BOOTSTRAP_CHARGING_TIME = 5 #значение в милисекундах
DEFAULT_VT_ON_TIME = 75             #значение в милисекундах
DEFAULT_DEADTIME = 1                #значение в милисекундах
DEFAULT_IN_VOLT_GOOD = 80           #значение в 0.1 В
DEFAULT_COIL_VOLT_GOOD = 160        #значение в 0.1 В
DEFAULT_VOLT_TRESHOLD = 5           #значение в 0.1 В
DEFAULT_CURR_TRESHOLD = 50          #значение в мА
DEFAULT_CURR_DEF_TIMES = 100        #кол-во проходов

#min and max settings
CONTROL_SOURCE_MAX_VALUE = 2      # /*источник управления 0-входы, 1-модбас, 2-смешанный*/
CONTROL_SOURCE_MIN_VALUE = 0
OWN_ID_MAX_VALUE = 255
OWN_ID_MIN_VALUE = 0
SERIAL_NUM_MAX_VALUE = 9999
SERIAL_NUM_MIN_VALUE = 0
CONVERT_COUNT_MAX = 50
CONVERT_COUNT_MIN = 1
PASS_CONVERT_COUNT_MAX = 10
PASS_CONVERT_COUNT_MIN = 0
BOOTSTRAP_CHARGING_TIME_MAX = 20
BOOTSTRAP_CHARGING_TIME_MIN = 1
VT_ON_TIME_MAX = 200
VT_ON_TIME_MIN = 30
DEADTIME_MAX = 10
DEADTIME_MIN = 1
IN_VOLT_GOOD_MAX = 150
IN_VOLT_GOOD_MIN = 50
COIL_VOLT_GOOD_MAX = 300
COIL_VOLT_GOOD_MIN = 60
VOLT_TRESHOLD_MAX = 10
VOLT_TRESHOLD_MIN = 1
CURR_TRESHOLD_MAX = 1000
CURR_TRESHOLD_MIN = 10
CURR_DEF_TIMES_MAX = 500
CURR_DEF_TIMES_MIN = 5

#default UART settings
DEFAULT_UART_OWN_ID = 1  #id устройства MODBUS
DEFAULT_UART_SPEED = 9600   #baudrate
DEFAULT_UART_PARITY = 0x04  # 0x00 - none; 0x04 - even; 0x06 - odd
DEFAULT_UART_STOPBITS = 0x00    # 0x00 - 1; 0x20 - 2; 0x30 - 1.5

#онстанты для бутлоадера
MAX_BIN_SYMBOLS = 28671      # максимальное количество символов в прошивке
BYTES_PER_PAGE = 128
MAIN_APP_OFFSET = 0
ACK = 0x79
NACK = 0x1F
BOOTLOADER_KEY_VALUE = [0xAA, 0xAA, 0x55, 0x55]
N_COMMAND = 0   # команда
NEG_N_COMMAND = 1   # команда
N_PAGE = 2  # номер страницы для записи
SIZE_MES = 3  # колчисетво байт далее
FIRST_BYTE_IN_MES = 3  # колчисетво байт далее
RM_Command = 0x11           # read memory
GO_Command = 0x21           # GO command
WM_Command = 0x31           # write memory
RESET_Command = 0x3A        # reset mcu
RESET_KEY_Command = 0xAB    # reset key word in mcu
SET_KEY_Command = 0xBB      # set key word in mcu

#настройки порта бутлоардера
BTL_PORT_SPEED = 19200
BTL_PORT_PARITY = 'E'
BTL_PORT_STOPBITS = 1
