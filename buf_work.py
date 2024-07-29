import struct
import functions
import const


def UnpuckAllSettingBuf(self, buf, len):
    u_buf = []
    if len == const.size_setttings_buf:
        u_buf = struct.unpack('4B7I6f11I2B', buf)
    else:
        u_buf = struct.unpack('4B7I6f1I2B', buf)
    print(u_buf)
    ParsAllSettings(self, u_buf, len)

    pass

def ParsAllSettings(self, buf, len):
    #проходим по всем элемнтам буфера и выставляем соответствующие значиня в GUI
    self.m_textCtrlSN_1.SetValue(str(buf[2]*256+buf[3]))
    self.m_comboBoxSS_1.SetSelection(buf[4])
    self.m_textCtrlMB_1.SetValue(str(buf[5]))
    self.m_comboBoxMB_1.SetSelection(self.m_comboBoxMB_1.FindString(str(buf[6])))
    stp_bits = {0x00: 0, 8192: 1, 8192: 2} # 0x00 - 1; 0x20 - 2; 8192 - 1.5
    self.m_comboBoxMB_2.SetSelection(stp_bits.get(buf[8], 0))
    prt_bits = {0x00: 0, 1024: 1, 1536: 2} # 0x00 - none; 1024 - even; 1536 - odd
    self.m_comboBoxMB_3.SetSelection(prt_bits.get(buf[9], 0))
    if len == const.size_setttings_buf:
        vers = str(buf[27])
        vers_u = vers[0] + '.' + vers[1] + '.' + vers[2] + vers[3]
    else:
        vers = str(buf[17])
        vers_u = vers[0] + '.' + vers[1] + '.' + vers[2] + vers[3]
    functions.AddTextLog(self, 'версия прошивки: ' + vers_u + '\n')
    self.m_textCtrl20.SetValue(str(buf[11]))
    self.m_textCtrl21.SetValue(str(buf[12]))
    self.m_textCtrl22.SetValue(str(buf[13]))
    self.m_textCtrl23.SetValue(str(buf[14]))
    self.m_textCtrl24.SetValue(str(buf[15]))
    self.m_textCtrl25.SetValue(str(buf[16]))
    if len == const.size_setttings_buf:
        self.m_textCtrl26.SetValue(str(buf[17]))
        self.m_textCtrl27.SetValue(str(buf[18]))
        self.m_textCtrl28.SetValue(str(buf[19]))
        self.m_textCtrl29.SetValue(str(buf[20]))
        self.m_textCtrl30.SetValue(str(buf[21]))
        self.m_textCtrl31.SetValue(str(buf[22]))
        self.m_textCtrl32.SetValue(str(buf[23]))
        self.m_textCtrl33.SetValue(str(buf[24]))
        self.m_textCtrl34.SetValue(str(buf[25]))
        self.m_textCtrl35.SetValue(str(buf[26]))
    pass

def PuckSettings(self):
    buf = []
    control_source = self.m_comboBoxSS_1.GetCurrentSelection()
    dev_id = int(self.m_textCtrlMB_1.GetValue())
    speed = int(self.m_comboBoxMB_1.GetValue())
    prt_bits = {0: 0x00, 1: 1024, 2: 1536} # 0x00 - none; 1024 - even; 1536 - odd
    prt = prt_bits.get(int(self.m_comboBoxMB_3.GetSelection()), 0x00)
    wordlenthbts = {0: 0x00, 1: 4096, 2: 4096} #0x00 - 8 bits word lenth, 0x10 - 9 bits word lenth
    wrdlenth = wordlenthbts.get(int(self.m_comboBoxMB_3.GetSelection()), 0x00)
    stop_bits = {0: 0x00, 1: 8192, 2: 0x30}  # 0x00 - 1; 0x20 - 2; 0x30 - 1.5
    stpbits = stop_bits.get(int(self.m_comboBoxMB_2.GetSelection()), 0x00)
    ser_num = int(self.m_textCtrlSN_1.GetValue())
    a1 = float(self.m_textCtrl20.GetValue())
    b1 = float(self.m_textCtrl21.GetValue())
    a2 = float(self.m_textCtrl22.GetValue())
    b2 = float(self.m_textCtrl23.GetValue())
    a3 = float(self.m_textCtrl24.GetValue())
    b3 = float(self.m_textCtrl25.GetValue())
    try:
        convert_count = int(self.m_textCtrl26.GetValue())
        pass_convert_count = int(self.m_textCtrl27.GetValue())
        bootstrap_charging_time = int(self.m_textCtrl28.GetValue())
        vt_on_time = int(self.m_textCtrl29.GetValue())
        dead_time = int(self.m_textCtrl30.GetValue())
        in_volt_good = int(self.m_textCtrl31.GetValue())
        coil_volt_good = int(self.m_textCtrl32.GetValue())
        volt_treshold = int(self.m_textCtrl33.GetValue())
        curr_treshold = int(self.m_textCtrl34.GetValue())
        curr_def_times = int(self.m_textCtrl35.GetValue())
    except:
        buf = struct.pack('<7I6f', control_source, dev_id, speed, wrdlenth, stpbits, prt, ser_num, a1, b1, a2, b2,
                          a3, b3)
    else:
        buf = struct.pack('<7I6f10I', control_source, dev_id, speed, wrdlenth, stpbits, prt, ser_num, a1, b1, a2, b2,
                          a3, b3,
                          convert_count, pass_convert_count, bootstrap_charging_time, vt_on_time, dead_time,
                          in_volt_good,
                          coil_volt_good, volt_treshold, curr_treshold, curr_def_times)

    print(buf)
    return buf

def CreateBufFromWorkSettings(self):
    buf = []
    tmp = 0
    # проходим по всем элемнтам GUI и выставляем соответствующие значиня в буфер
    buf.append(self.m_comboBoxSS_1.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_2.GetCurrentSelection()+1)

    buf.append(int(self.m_textCtrlSS_1.GetValue()))

    buf.append(int(self.m_textCtrlSS_2.GetValue()))

    buf.append(int(self.m_textCtrlSS_3.GetValue()) // 256)
    buf.append(int(self.m_textCtrlSS_3.GetValue()) % 256)

    buf.append(int(self.m_textCtrlSS_4.GetValue()) // 256)
    buf.append(int(self.m_textCtrlSS_4.GetValue()) % 256)

    buf.append(self.m_comboBoxSS_3.GetCurrentSelection()+1)
    buf.append(self.m_comboBoxSS_4.GetCurrentSelection()+1)
    buf.append(self.m_comboBoxSS_5.GetCurrentSelection()+1)
    buf.append(self.m_comboBoxSS_6.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_7.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_8.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_9.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_10.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_11.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_12.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_13.GetCurrentSelection())
    buf.append(self.m_comboBoxSS_14.GetCurrentSelection())
    buf.append(10)
    buf.append(self.m_comboBoxSS_15.GetCurrentSelection())
    return buf



