# тут все функции для отображения в гуи
import const

def EnableSettingsStructItems(self):

    pass

def ShowComSettings(self, ser):
    self.m_staticTextCom6.SetLabel(ser.port)
    self.m_staticTextCom7.SetLabel(str(ser.baudrate))
    if ser.parity == 'N':
        self.m_staticTextCom8.SetLabel('нет')
    elif ser.parity == 'E':
        self.m_staticTextCom8.SetLabel('чет')
    elif ser.parity == 'O':
        self.m_staticTextCom8.SetLabel('нечет')
    self.m_staticTextCom9.SetLabel(str(ser.stopbits))
    self.m_staticTextCom10.SetLabel('подключен')
    pass

def HideComSettings(self):
    self.m_staticTextCom6.SetLabel('--')
    self.m_staticTextCom7.SetLabel('--')
    self.m_staticTextCom8.SetLabel('--')
    self.m_staticTextCom9.SetLabel('--')
    self.m_staticTextCom10.SetLabel('--')
    pass

def ShowDeviseSettings(self):
    self.m_comboBoxSS_1.Enabled = True
    if self.m_checkBox1.GetValue() == True:
        self.m_comboBoxSS_1.Enabled = True
        self.m_textCtrl20.Enabled = True
        self.m_textCtrl21.Enabled = True
        self.m_textCtrl22.Enabled = True
        self.m_textCtrl23.Enabled = True
        self.m_textCtrl24.Enabled = True
        self.m_textCtrl25.Enabled = True
        self.m_textCtrl26.Enabled = True
        self.m_textCtrl27.Enabled = True
        self.m_textCtrl28.Enabled = True
        self.m_textCtrl29.Enabled = True
        self.m_textCtrl30.Enabled = True
        self.m_textCtrl31.Enabled = True
        self.m_textCtrl32.Enabled = True
        self.m_textCtrl33.Enabled = True
        self.m_textCtrl34.Enabled = True
        self.m_textCtrl35.Enabled = True
    pass

def HideDeviseSettings(self):
    self.m_comboBoxSS_1.Enabled = False
    self.m_textCtrl20.Enabled = False
    self.m_textCtrl21.Enabled = False
    self.m_textCtrl22.Enabled = False
    self.m_textCtrl23.Enabled = False
    self.m_textCtrl24.Enabled = False
    self.m_textCtrl25.Enabled = False
    self.m_textCtrl26.Enabled = False
    self.m_textCtrl27.Enabled = False
    self.m_textCtrl28.Enabled = False
    self.m_textCtrl29.Enabled = False
    self.m_textCtrl30.Enabled = False
    self.m_textCtrl31.Enabled = False
    self.m_textCtrl32.Enabled = False
    self.m_textCtrl33.Enabled = False
    self.m_textCtrl34.Enabled = False
    self.m_textCtrl35.Enabled = False
    pass

def ShowDeviseModbusSettings(self):
    self.m_textCtrlMB_1.Enabled = True
    self.m_comboBoxMB_1.Enabled = True
    self.m_comboBoxMB_2.Enabled = True
    self.m_comboBoxMB_3.Enabled = True
    self.m_buttonMB_1.Enabled = True
    self.m_buttonMB_2.Enabled = True
    self.m_buttonQS_1.Enabled = True
    self.m_buttonQS_2.Enabled = True
    self.m_buttonQS_3.Enabled = True
    self.m_buttonQS_4.Enabled = True
    self.m_buttonQS_5.Enabled = True
    self.m_buttonQS_6.Enabled = True
    self.m_buttonQS_7.Enabled = True
    self.m_buttonQS_8.Enabled = True
    pass

def HideDeviseModbusSettings(self):
    self.m_textCtrlMB_1.Enabled = False
    self.m_comboBoxMB_1.Enabled = False
    self.m_comboBoxMB_2.Enabled = False
    self.m_comboBoxMB_3.Enabled = False
    self.m_buttonMB_1.Enabled = False
    self.m_buttonMB_2.Enabled = False
    self.m_buttonQS_1.Enabled = False
    self.m_buttonQS_2.Enabled = False
    self.m_buttonQS_3.Enabled = False
    self.m_buttonQS_4.Enabled = False
    self.m_buttonQS_5.Enabled = False
    self.m_buttonQS_6.Enabled = False
    self.m_buttonQS_7.Enabled = False
    self.m_buttonQS_8.Enabled = False
    pass

def ShowDefaultModbusSetting(self):
    self.m_textCtrlMB_1.SetValue(str(const.DEFAULT_UART_OWN_ID))
    self.m_comboBoxMB_1.SetSelection(2)
    self.m_comboBoxMB_2.SetSelection(0)
    self.m_comboBoxMB_3.SetSelection(1)
    self.m_comboBoxSS_1.SetSelection(0)

    pass

def ShowDefaultWorkSetting(self):
    self.m_comboBoxSS_1.SetSelection(0)
    self.m_textCtrl20.SetValue(str(const.DEFAULT_A1))
    self.m_textCtrl21.SetValue(str(const.DEFAULT_B1))
    self.m_textCtrl22.SetValue(str(const.DEFAULT_A2))
    self.m_textCtrl23.SetValue(str(const.DEFAULT_B2))
    self.m_textCtrl24.SetValue(str(const.DEFAULT_A3))
    self.m_textCtrl25.SetValue(str(const.DEFAULT_B3))
    self.m_textCtrl26.SetValue(str(const.DEFAULT_CONVERT_COUNT))
    self.m_textCtrl27.SetValue(str(const.DEFAULT_PASS_CONVERT_COUNT))
    self.m_textCtrl28.SetValue(str(const.DEFAULT_BOOTSTRAP_CHARGING_TIME))
    self.m_textCtrl29.SetValue(str(const.DEFAULT_VT_ON_TIME))
    self.m_textCtrl30.SetValue(str(const.DEFAULT_DEADTIME))
    self.m_textCtrl31.SetValue(str(const.DEFAULT_IN_VOLT_GOOD))
    self.m_textCtrl32.SetValue(str(const.DEFAULT_COIL_VOLT_GOOD))
    self.m_textCtrl33.SetValue(str(const.DEFAULT_VOLT_TRESHOLD))
    self.m_textCtrl34.SetValue(str(const.DEFAULT_CURR_TRESHOLD))
    self.m_textCtrl35.SetValue(str(const.DEFAULT_CURR_DEF_TIMES))
    pass

def ShowSnRstSettings(self):
    self.m_buttonSN_1.Enabled = True
    self.m_buttonRST_1.Enabled = True
    if self.m_checkBox1.GetValue() == True:
        self.m_textCtrlSN_1.Enabled = True
    pass

def HideSnRstSettings(self):
    self.m_textCtrlSN_1.Enabled = False
    self.m_buttonSN_1.Enabled = False
    self.m_buttonRST_1.Enabled = False
    pass