import wx


class CustomMineDialog(wx.Dialog):
    def __init__(self, parent):
        super(CustomMineDialog, self).__init__(parent, title="自定义雷数", size=(300, 200))
        self.parent = parent
        self.default_mines = parent.numMine

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='雷数 (1-99):')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.tc = wx.SpinCtrl(panel, value=str(self.default_mines), min=1, max=99)
        hbox1.Add(self.tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(panel, label='确定', id=wx.ID_OK)
        cancelButton = wx.Button(panel, label='取消', id=wx.ID_CANCEL)
        hbox2.Add(okButton)
        hbox2.Add(cancelButton, flag=wx.LEFT, border=5)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        panel.SetSizer(vbox)

        okButton.Bind(wx.EVT_BUTTON, self.OnOk)
        cancelButton.Bind(wx.EVT_BUTTON, self.OnCancel)

    def OnOk(self, event):
        try:
            mine_count = int(self.tc.GetValue())
            if 1 <= mine_count <= 99:
                self.parent.numMine = mine_count
                self.parent.setNewGame(mine_count)
                self.Destroy()
            else:
                wx.MessageBox("请输入1-99之间的数字", "错误", wx.OK | wx.ICON_ERROR)
        except ValueError:
            wx.MessageBox("请输入有效的数字", "错误", wx.OK | wx.ICON_ERROR)

    def OnCancel(self, event):
        self.Destroy()
