import wx
import noname
import functions
from threading import Thread
import GUI_HID
import const


class MyFrame2(noname.MyFrame2):

    def __init__(self, parent):
        noname.MyFrame2.__init__(self, parent)

    def CloseFrame2(self, e):
        self.Close()

class Main_window(noname.MyFrame1):
    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)
        th1 = Thread(target=functions.ControlCurrentConnectionState, args=(self, ), daemon=True)
        th1.start()
        GUI_HID.EnableSettingsStructItems(self)
        self.OpenedFile = 0
        self.OpenedFileLenth = 0
        self.OpenedFileFullPages = 0
        self.last_page_bytes = 0

    def FileDialogOpen(self, e):
        FD = wx.FileDialog(self, "Открыть файл: ", wildcard="bin файлы (*.bin)|*bin", style=wx.FD_OPEN)
        if FD.ShowModal() == wx.ID_CANCEL:
            return
        pathname = FD.GetPath()
        f = open(pathname, 'rb')
        self.OpenedFile = f.read()
        f.close()
        self.OpenedFileLenth = len(self.OpenedFile)
        if self.OpenedFileLenth >= const.MAX_BIN_SYMBOLS:
            self.OpenedFileLenth = 0
            functions.AddTextLog(self, 'слишком большой файл прошивки\n')
            self.m_button6.Disable()
            return
        #проверка файла на совместимость с стм8
        for i in range(0,40,4):
            if self.OpenedFile[i] != 0x82:
                functions.AddTextLog(self, 'не подходящий файл\n')
                self.m_button6.Disable()
                return
        self.m_staticText401.SetLabel(pathname)
        self.m_button6.Enable()
        self.m_gauge1.Enable()
        self.OpenedFileFullPages = self.OpenedFileLenth // const.BYTES_PER_PAGE
        self.last_page_bytes = (self.OpenedFileLenth - (self.OpenedFileFullPages * const.BYTES_PER_PAGE))
        functions.AddTextLog(self, 'выбран файл:\n' + pathname + '\n')
        functions.AddTextLog(self, 'символов: ' + str(self.OpenedFileLenth))
        functions.AddTextLog(self, '\nстраниц: ' + str(self.OpenedFileFullPages + 1) + '\n')

    def SendModbusSettings(self, e):
        functions.SendModbusSettings(self)
        functions.sleep(0.3)

    def SendModbusDefaultSettings(self, e):
        functions.SendModbusDefaultSettings(self)

    def SendWorkSettings(self, e):
        functions.SendWorkSettings(self)

    def SendDefaultWorkSettings(self, e):
        functions.SendDefaultWorkSettings(self)

    def SendReadAllSettings(self, e):
        functions.SendReadAllSettings(self)

    def SendResetMcu(self, e):
        functions.SendResetMcu(self)

    def TextCtrlCheckDigit(self, e):
        functions.TextCtrlCheckDigit(self, e)
        pass

    def PressComButton(self, e):
        functions.PressComButton(self)

    def InsertPassword( self, event ):
        functions.InsertPassword(self)

    def btn_apps_id12_coil24( self, e ):
        functions.btn_apps_id12_coil24(self)

    def btn_apps_id15_coil24( self, e ):
        functions.btn_apps_id15_coil24(self)

    def btn_apps_id14_coil24( self, e ):
        functions.btn_apps_id14_coil24(self)

    def btn_apps_id17_coil24( self, e ):
        functions.btn_apps_id17_coil24(self)

    def btn_apps_id12_coil12( self, e ):
        functions.btn_apps_id12_coil12(self)

    def btn_apps_id15_coil12( self, e ):
        functions.btn_apps_id15_coil12(self)

    def btn_apps_id14_coil12( self, e ):
        functions.btn_apps_id14_coil12(self)

    def btn_apps_id17_coil12( self, e ):
        functions.btn_apps_id17_coil12(self)

    def ShowMyFrame2(self, e):
        FD = MyFrame2(self)
        FD.IsTopLevel()
        FD.Show()



app = wx.App(False)
frame = Main_window(None)
frame.Show(True)
app.MainLoop()