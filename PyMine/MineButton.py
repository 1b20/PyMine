import wx
from Util import imgSize, getImg

class MineButton(wx.BitmapButton):
    col = 0
    row = 0
    flag = 0
    clickFlag = False

    def __init__(self,parent,row, col, ticon):
        wx.BitmapButton.__init__(self,parent,size=(34,34),bitmap=imgSize(ticon,34,34),style=wx.BORDER_NONE)
        self.icon = ticon
        self.row = row
        self.col = col

    def getClickFlag (self) :
        return(self.clickFlag)

    def setClickFlag(self, toSet) :
        self.clickFlag = toSet

    def getCol(self) :
        return(self.col)

    def getRow(self):
        return(self.row)

    def setFlag(self,flag) :
        self.flag = flag

    def getFlag(self):
        return(self.flag)

    def setIcon(self, ticon):
        self.icon = ticon
        self.SetBitmapLabel(imgSize(ticon,34,34))

def main():
    app = wx.App()
    frame = wx.Frame(None)
    pane = wx.Panel(frame)
    button = MineButton(pane,3,3,wx.Bitmap(getImg("3.gif")))
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
