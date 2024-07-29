# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"КЭМИ М2 - утилита настройки", pos = wx.DefaultPosition, size = wx.Size( 1190,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 1190,700 ), wx.DefaultSize )
		self.SetExtraStyle( wx.FRAME_EX_METAL )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Справка", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem1 )
		
		self.m_menubar1.Append( self.m_menu1, u"Меню" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2.SetMinSize( wx.Size( 500,400 ) ) 
		self.m_logTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,600 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH )
		self.m_logTextCtrl.SetMinSize( wx.Size( 300,400 ) )
		self.m_logTextCtrl.SetMaxSize( wx.Size( 600,-1 ) )
		
		bSizer2.Add( self.m_logTextCtrl, 1, wx.ALL|wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticTextCom1 = wx.StaticText( self, wx.ID_ANY, u"Текущие настройки COM порта:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom1.Wrap( -1 )
		bSizer9.Add( self.m_staticTextCom1, 0, wx.ALL, 5 )
		
		gSizer2 = wx.GridSizer( 2, 6, 0, 0 )
		
		self.m_staticTextCom2 = wx.StaticText( self, wx.ID_ANY, u"порт:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom2.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom2, 0, wx.ALL, 5 )
		
		self.m_staticTextCom3 = wx.StaticText( self, wx.ID_ANY, u"скорость:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom3.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom3, 0, wx.ALL, 5 )
		
		self.m_staticTextCom4 = wx.StaticText( self, wx.ID_ANY, u"четность:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom4.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom4, 0, wx.ALL, 5 )
		
		self.m_staticTextCom5 = wx.StaticText( self, wx.ID_ANY, u"стоп-биты:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom5.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom5, 0, wx.ALL, 5 )
		
		self.m_staticTextCom5 = wx.StaticText( self, wx.ID_ANY, u"состояние:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom5.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom5, 0, wx.ALL, 5 )
		
		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		gSizer2.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.m_staticTextCom6 = wx.StaticText( self, wx.ID_ANY, u"- -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom6.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom6, 0, wx.ALL, 5 )
		
		self.m_staticTextCom7 = wx.StaticText( self, wx.ID_ANY, u"- -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom7.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom7, 0, wx.ALL, 5 )
		
		self.m_staticTextCom8 = wx.StaticText( self, wx.ID_ANY, u"- -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom8.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom8, 0, wx.ALL, 5 )
		
		self.m_staticTextCom9 = wx.StaticText( self, wx.ID_ANY, u"- -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom9.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom9, 0, wx.ALL, 5 )
		
		self.m_staticTextCom10 = wx.StaticText( self, wx.ID_ANY, u"- -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCom10.Wrap( -1 )
		gSizer2.Add( self.m_staticTextCom10, 0, wx.ALL, 5 )
		
		self.m_buttonCOM_1 = wx.Button( self, wx.ID_ANY, u"поиск устройства", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_buttonCOM_1, 1, wx.ALL, 5 )
		
		
		bSizer9.Add( gSizer2, 0, 0, 5 )
		
		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer9.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticTextSS_1 = wx.StaticText( self, wx.ID_ANY, u"Настройки режима работы:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_1.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_1, 0, wx.ALL, 5 )
		
		self.m_staticText371 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText371.Wrap( -1 )
		fgSizer1.Add( self.m_staticText371, 0, wx.ALL, 5 )
		
		self.m_staticText56 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )
		fgSizer1.Add( self.m_staticText56, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_2 = wx.StaticText( self, wx.ID_ANY, u"источник управления:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_2.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_2, 0, wx.ALL, 5 )
		
		m_comboBoxSS_1Choices = [ u"входы", u"MODBUS", u"смешанный" ]
		self.m_comboBoxSS_1 = wx.ComboBox( self, wx.ID_ANY, u"входы", wx.DefaultPosition, wx.DefaultSize, m_comboBoxSS_1Choices, wx.CB_READONLY )
		self.m_comboBoxSS_1.SetSelection( 0 )
		self.m_comboBoxSS_1.SetMinSize( wx.Size( 110,-1 ) )
		
		fgSizer1.Add( self.m_comboBoxSS_1, 0, 0, 5 )
		
		self.m_staticText57 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )
		fgSizer1.Add( self.m_staticText57, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_3 = wx.StaticText( self, wx.ID_ANY, u"коэффициент А1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_3.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_3, 0, wx.ALL, 5 )
		
		self.m_textCtrl20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl20.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl20, 0, 0, 5 )
		
		self.m_staticText37117 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37117.Wrap( -1 )
		fgSizer1.Add( self.m_staticText37117, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_4 = wx.StaticText( self, wx.ID_ANY, u"коэффициент Б1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_4.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_4, 0, wx.ALL, 5 )
		
		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl21.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl21, 0, 0, 5 )
		
		self.m_staticText37116 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37116.Wrap( -1 )
		fgSizer1.Add( self.m_staticText37116, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_5 = wx.StaticText( self, wx.ID_ANY, u"коэффициент А2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_5.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_5, 0, wx.ALL, 5 )
		
		self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl22.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl22, 0, 0, 5 )
		
		self.m_staticText37115 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37115.Wrap( -1 )
		fgSizer1.Add( self.m_staticText37115, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_6 = wx.StaticText( self, wx.ID_ANY, u"коэффициент Б2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_6.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_6, 0, wx.ALL, 5 )
		
		self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl23.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl23, 0, 0, 5 )
		
		self.m_staticText37114 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37114.Wrap( -1 )
		fgSizer1.Add( self.m_staticText37114, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_61 = wx.StaticText( self, wx.ID_ANY, u"коэффициент А3:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_61.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_61, 0, wx.ALL, 5 )
		
		self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl24.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl24, 0, 0, 5 )
		
		self.m_staticText37113 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37113.Wrap( -1 )
		fgSizer1.Add( self.m_staticText37113, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_62 = wx.StaticText( self, wx.ID_ANY, u"коэффициент Б3:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_62.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_62, 0, wx.ALL, 5 )
		
		self.m_textCtrl25 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl25.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl25, 0, 0, 5 )
		
		self.m_staticText37112 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37112.Wrap( -1 )
		fgSizer1.Add( self.m_staticText37112, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_622 = wx.StaticText( self, wx.ID_ANY, u"кол-во измерений АЦП:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_622.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_622, 0, wx.ALL, 5 )
		
		self.m_textCtrl26 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl26.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl26, 0, 0, 5 )
		
		self.m_staticText37111 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37111.Wrap( -1 )
		fgSizer1.Add( self.m_staticText37111, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_623 = wx.StaticText( self, wx.ID_ANY, u"кол-во пропускаемых измерений АЦП:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_623.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_623, 0, wx.ALL, 5 )
		
		self.m_textCtrl27 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl27.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl27, 0, 0, 5 )
		
		self.m_staticText37110 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37110.Wrap( -1 )
		fgSizer1.Add( self.m_staticText37110, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_624 = wx.StaticText( self, wx.ID_ANY, u"время заряда bootstrap конденсаторов:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_624.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_624, 0, wx.ALL, 5 )
		
		self.m_textCtrl28 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl28.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl28, 0, 0, 5 )
		
		self.m_staticText3719 = wx.StaticText( self, wx.ID_ANY, u"мс", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3719.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3719, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_6241 = wx.StaticText( self, wx.ID_ANY, u"время вкл-го состояния транзисторов:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_6241.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_6241, 0, wx.ALL, 5 )
		
		self.m_textCtrl29 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl29.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl29, 0, 0, 5 )
		
		self.m_staticText3718 = wx.StaticText( self, wx.ID_ANY, u"мс", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3718.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3718, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_62411 = wx.StaticText( self, wx.ID_ANY, u"мертвое время:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_62411.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_62411, 0, wx.ALL, 5 )
		
		self.m_textCtrl30 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl30.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl30, 0, 0, 5 )
		
		self.m_staticText3717 = wx.StaticText( self, wx.ID_ANY, u"мс", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3717.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3717, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_62412 = wx.StaticText( self, wx.ID_ANY, u"предел нормального вохдного напр-я:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_62412.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_62412, 0, wx.ALL, 5 )
		
		self.m_textCtrl31 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl31.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl31, 0, 0, 5 )
		
		self.m_staticText3716 = wx.StaticText( self, wx.ID_ANY, u"0.1В", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3716.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3716, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_62413 = wx.StaticText( self, wx.ID_ANY, u"предел нормального напр-я катушки:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_62413.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_62413, 0, wx.ALL, 5 )
		
		self.m_textCtrl32 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl32.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl32, 0, 0, 5 )
		
		self.m_staticText3715 = wx.StaticText( self, wx.ID_ANY, u"0.1В", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3715.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3715, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_62414 = wx.StaticText( self, wx.ID_ANY, u"добавочный порог нормального напр-я:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_62414.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_62414, 0, wx.ALL, 5 )
		
		self.m_textCtrl33 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl33.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl33, 0, 0, 5 )
		
		self.m_staticText3714 = wx.StaticText( self, wx.ID_ANY, u"0.1В", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3714.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3714, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_62415 = wx.StaticText( self, wx.ID_ANY, u"порог тока:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_62415.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_62415, 0, wx.ALL, 5 )
		
		self.m_textCtrl34 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl34.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl34, 0, 0, 5 )
		
		self.m_staticText3713 = wx.StaticText( self, wx.ID_ANY, u"мА", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3713.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3713, 0, wx.ALL, 5 )
		
		self.m_staticTextSS_624161 = wx.StaticText( self, wx.ID_ANY, u"кол-во измерений тока катушки:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSS_624161.Wrap( -1 )
		fgSizer1.Add( self.m_staticTextSS_624161, 0, wx.ALL, 5 )
		
		self.m_textCtrl35 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl35.Enable( False )
		
		fgSizer1.Add( self.m_textCtrl35, 0, 0, 5 )
		
		self.m_staticText3712 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3712.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3712, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer4.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		gSizer3 = wx.GridSizer( 16, 2, 2, 0 )
		
		gSizer3.SetMinSize( wx.Size( 300,300 ) ) 
		self.m_staticTextMB_1 = wx.StaticText( self, wx.ID_ANY, u"Настройки MODBUS:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMB_1.Wrap( -1 )
		gSizer3.Add( self.m_staticTextMB_1, 0, wx.ALL, 5 )
		
		self.m_staticText381 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText381.Wrap( -1 )
		gSizer3.Add( self.m_staticText381, 0, wx.ALL, 5 )
		
		self.m_staticTextMB_2 = wx.StaticText( self, wx.ID_ANY, u"ID устройства:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMB_2.Wrap( -1 )
		gSizer3.Add( self.m_staticTextMB_2, 0, wx.ALL, 5 )
		
		self.m_textCtrlMB_1 = wx.TextCtrl( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlMB_1.Enable( False )
		self.m_textCtrlMB_1.SetMaxSize( wx.Size( 80,-1 ) )
		
		gSizer3.Add( self.m_textCtrlMB_1, 0, wx.ALL, 5 )
		
		self.m_staticTextMB_3 = wx.StaticText( self, wx.ID_ANY, u"скорость:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMB_3.Wrap( -1 )
		gSizer3.Add( self.m_staticTextMB_3, 0, wx.ALL, 5 )
		
		m_comboBoxMB_1Choices = [ u"2400", u"4800", u"9600", u"19200", u"38600" ]
		self.m_comboBoxMB_1 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxMB_1Choices, wx.CB_READONLY )
		self.m_comboBoxMB_1.SetSelection( 0 )
		self.m_comboBoxMB_1.Enable( False )
		self.m_comboBoxMB_1.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer3.Add( self.m_comboBoxMB_1, 0, wx.ALL, 5 )
		
		self.m_staticTextMB_4 = wx.StaticText( self, wx.ID_ANY, u"стоп-биты", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMB_4.Wrap( -1 )
		gSizer3.Add( self.m_staticTextMB_4, 0, wx.ALL, 5 )
		
		m_comboBoxMB_2Choices = [ u"1", u"2", u"1.5" ]
		self.m_comboBoxMB_2 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxMB_2Choices, wx.CB_READONLY )
		self.m_comboBoxMB_2.SetSelection( 2 )
		self.m_comboBoxMB_2.Enable( False )
		self.m_comboBoxMB_2.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer3.Add( self.m_comboBoxMB_2, 0, wx.ALL, 5 )
		
		self.m_staticTextMB_5 = wx.StaticText( self, wx.ID_ANY, u"четность:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMB_5.Wrap( -1 )
		gSizer3.Add( self.m_staticTextMB_5, 0, wx.ALL, 5 )
		
		m_comboBoxMB_3Choices = [ u"нет", u"чет", u"нечет" ]
		self.m_comboBoxMB_3 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxMB_3Choices, wx.CB_READONLY )
		self.m_comboBoxMB_3.SetSelection( 0 )
		self.m_comboBoxMB_3.Enable( False )
		self.m_comboBoxMB_3.SetMinSize( wx.Size( 80,-1 ) )
		
		gSizer3.Add( self.m_comboBoxMB_3, 0, wx.ALL, 5 )
		
		self.m_staticTextSN_1 = wx.StaticText( self, wx.ID_ANY, u"серийный номер:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSN_1.Wrap( -1 )
		gSizer3.Add( self.m_staticTextSN_1, 0, wx.ALL, 5 )
		
		self.m_textCtrlSN_1 = wx.TextCtrl( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlSN_1.Enable( False )
		self.m_textCtrlSN_1.SetMaxSize( wx.Size( 80,-1 ) )
		
		gSizer3.Add( self.m_textCtrlSN_1, 0, wx.ALL, 5 )
		
		self.m_buttonSN_1 = wx.Button( self, wx.ID_ANY, u"прочитать настройки", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSN_1.Enable( False )
		
		gSizer3.Add( self.m_buttonSN_1, 0, wx.ALL, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		self.m_buttonMB_1 = wx.Button( self, wx.ID_ANY, u"настройки от производителя", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonMB_1.Enable( False )
		
		gSizer3.Add( self.m_buttonMB_1, 0, wx.ALL, 5 )
		
		self.m_buttonMB_2 = wx.Button( self, wx.ID_ANY, u"записать значения в устройство", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonMB_2.Enable( False )
		
		gSizer3.Add( self.m_buttonMB_2, 0, wx.ALL, 5 )
		
		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline11.SetMinSize( wx.Size( 180,-1 ) )
		
		gSizer3.Add( self.m_staticline11, 1, wx.ALL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_staticline10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_staticline10.SetMinSize( wx.Size( 180,-1 ) )
		
		gSizer3.Add( self.m_staticline10, 0, wx.ALL, 5 )
		
		self.m_staticText60 = wx.StaticText( self, wx.ID_ANY, u"Быстрые настройки:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )
		gSizer3.Add( self.m_staticText60, 0, wx.ALL, 5 )
		
		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		gSizer3.Add( self.m_staticText61, 0, wx.ALL, 5 )
		
		self.m_buttonQS_1 = wx.Button( self, wx.ID_ANY, u"АППС id12 катушка 24В", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonQS_1.Enable( False )
		
		gSizer3.Add( self.m_buttonQS_1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_buttonQS_2 = wx.Button( self, wx.ID_ANY, u"АППС id12 катушка 12В", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonQS_2.Enable( False )
		
		gSizer3.Add( self.m_buttonQS_2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_buttonQS_3 = wx.Button( self, wx.ID_ANY, u"АППС id14 катушка 24В", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonQS_3.Enable( False )
		
		gSizer3.Add( self.m_buttonQS_3, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_buttonQS_4 = wx.Button( self, wx.ID_ANY, u"АППС id14 катушка 12В", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonQS_4.Enable( False )
		
		gSizer3.Add( self.m_buttonQS_4, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_buttonQS_5 = wx.Button( self, wx.ID_ANY, u"АППС id15 катушка 24В", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonQS_5.Enable( False )
		
		gSizer3.Add( self.m_buttonQS_5, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_buttonQS_6 = wx.Button( self, wx.ID_ANY, u"АППС id15 катушка 12В", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonQS_6.Enable( False )
		
		gSizer3.Add( self.m_buttonQS_6, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_buttonQS_7 = wx.Button( self, wx.ID_ANY, u"АППС id17 катушка 24В", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonQS_7.Enable( False )
		
		gSizer3.Add( self.m_buttonQS_7, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_buttonQS_8 = wx.Button( self, wx.ID_ANY, u"АППС id17 катушка 12В", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonQS_8.Enable( False )
		
		gSizer3.Add( self.m_buttonQS_8, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline101 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_staticline101.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_staticline101.SetMinSize( wx.Size( 180,-1 ) )
		
		gSizer3.Add( self.m_staticline101, 0, wx.ALL, 5 )
		
		self.m_staticline102 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline102.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_staticline102.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_staticline102.SetMinSize( wx.Size( 180,-1 ) )
		
		gSizer3.Add( self.m_staticline102, 0, wx.ALL, 5 )
		
		self.m_buttonRST_1 = wx.Button( self, wx.ID_ANY, u"перезагрузить MCU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonRST_1.Enable( False )
		
		gSizer3.Add( self.m_buttonRST_1, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( gSizer3, 0, 0, 2 )
		
		self.m_staticline12 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer4.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer4, 1, wx.ALL, 5 )
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer9.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Версия программы: 1.3", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText49.Wrap( -1 )
		bSizer6.Add( self.m_staticText49, 1, wx.ALL|wx.RIGHT, 5 )
		
		
		bSizer9.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.ShowMyFrame2, id = self.m_menuItem1.GetId() )
		self.m_buttonCOM_1.Bind( wx.EVT_BUTTON, self.PressComButton )
		self.m_textCtrlMB_1.Bind( wx.EVT_TEXT, self.TextCtrlCheckDigit )
		self.m_textCtrlSN_1.Bind( wx.EVT_TEXT, self.TextCtrlCheckDigit )
		self.m_buttonSN_1.Bind( wx.EVT_BUTTON, self.SendReadAllSettings )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.InsertPassword )
		self.m_buttonMB_1.Bind( wx.EVT_BUTTON, self.SendModbusDefaultSettings )
		self.m_buttonMB_2.Bind( wx.EVT_BUTTON, self.SendModbusSettings )
		self.m_buttonQS_1.Bind( wx.EVT_BUTTON, self.btn_apps_id12_coil24 )
		self.m_buttonQS_2.Bind( wx.EVT_BUTTON, self.btn_apps_id12_coil12 )
		self.m_buttonQS_3.Bind( wx.EVT_BUTTON, self.btn_apps_id14_coil24 )
		self.m_buttonQS_4.Bind( wx.EVT_BUTTON, self.btn_apps_id14_coil12 )
		self.m_buttonQS_5.Bind( wx.EVT_BUTTON, self.btn_apps_id15_coil24 )
		self.m_buttonQS_6.Bind( wx.EVT_BUTTON, self.btn_apps_id15_coil12 )
		self.m_buttonQS_7.Bind( wx.EVT_BUTTON, self.btn_apps_id17_coil24 )
		self.m_buttonQS_8.Bind( wx.EVT_BUTTON, self.btn_apps_id17_coil12 )
		self.m_buttonRST_1.Bind( wx.EVT_BUTTON, self.SendResetMcu )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ShowMyFrame2( self, event ):
		event.Skip()
	
	def PressComButton( self, event ):
		event.Skip()
	
	def TextCtrlCheckDigit( self, event ):
		event.Skip()
	
	
	def SendReadAllSettings( self, event ):
		event.Skip()
	
	def InsertPassword( self, event ):
		event.Skip()
	
	def SendModbusDefaultSettings( self, event ):
		event.Skip()
	
	def SendModbusSettings( self, event ):
		event.Skip()
	
	def btn_apps_id12_coil24( self, event ):
		event.Skip()
	
	def btn_apps_id12_coil12( self, event ):
		event.Skip()
	
	def btn_apps_id14_coil24( self, event ):
		event.Skip()
	
	def btn_apps_id14_coil12( self, event ):
		event.Skip()
	
	def btn_apps_id15_coil24( self, event ):
		event.Skip()
	
	def btn_apps_id15_coil12( self, event ):
		event.Skip()
	
	def btn_apps_id17_coil24( self, event ):
		event.Skip()
	
	def btn_apps_id17_coil12( self, event ):
		event.Skip()
	
	def SendResetMcu( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Справка", pos = wx.DefaultPosition, size = wx.Size( 500,350 ), style = wx.CAPTION|wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 500,350 ), wx.DefaultSize )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText62 = wx.StaticText( self, wx.ID_ANY, u"В начале работы необходимо подключиться данной утилитой к устройству КЭМИ М2. Устройство должно быть подключенно к ПК через преобразователь USB->RS485.\nПри нажатии на кнопку \"поиск устройства\" утилита автоматически ищет во всех доступных портах поддерживаемое устройство и в случае нахождения считывает все его текущие настройки и выводит соответствующие сообщения в текстовое поле с левой стороны. Становятся доступны для редактирования параметры порта, ID устройства на шине Modbus и источник управления. Остальные настройки доступны для редактирования только в режиме администратора.\nПри редактировани каких либо настроек необходимо записать значения в устройство с помощью кнопки \"записать значения в устройство\". При нажатии на кнопку \"настройки от производителя\" все поля с настройками заполняются значениями по умолчанию и сразу отправляются в устройство. Кнопки быстрых настроек заполняют поля заранее подготовленными значениями и отправляют в устройство.\nУстройство начинает работать с новыми значениями только после перезагрузки. При смене серийного номера перезагрузка происходит автоматически.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )
		bSizer6.Add( self.m_staticText62, 1, wx.ALL, 10 )
		
		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Ок", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button18.Bind( wx.EVT_BUTTON, self.CloseFrame2 )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def CloseFrame2( self, event ):
		event.Skip()
	

