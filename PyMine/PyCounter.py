#!python 
import wx
from Util import imgSize, getImg

class PyCounter(wx.Panel):
    counter = []
    __numSet = []
    counterNum = 0

    def __init__(self,parent, num):
        wx.Panel.__init__(self,parent,size=(78,50),name="PyCounter Test")
        self.numSet =  [ wx.Bitmap(getImg("c0.gif")), wx.Bitmap(getImg("c1.gif")),
                        wx.Bitmap(getImg("c2.gif")), wx.Bitmap(getImg("c3.gif")),
                        wx.Bitmap(getImg("c4.gif")), wx.Bitmap(getImg("c5.gif")),
                        wx.Bitmap(getImg("c6.gif")), wx.Bitmap(getImg("c7.gif")),
                        wx.Bitmap(getImg("c8.gif")), wx.Bitmap(getImg("c9.gif"))]

        self.counterNum = num

        ones = self.counterNum % 10
        tens = self.counterNum % 100 // 10
        hundreds = self.counterNum % 1000 // 100

        #print "%d : %d : %d" % (hundreds, tens, ones)

        self.counter = [ wx.BitmapButton(self,-1,bitmap=imgSize(self.numSet[hundreds],26,46),size=(26,46),style=wx.BORDER_NONE),
                         wx.BitmapButton(self,-1,bitmap=imgSize(self.numSet[tens],26,46),size=(26,46),style=wx.BORDER_NONE),
                         wx.BitmapButton(self,-1,bitmap=imgSize(self.numSet[ones],26,46), size=(26,46),style=wx.BORDER_NONE)]

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        for i in range(0,3):
            hbox.Add(self.counter[i])

        self.SetSizerAndFit(hbox)
        self.Center()
        self.Show()

    def getCounterNum(self):
        return(self.counterNum)

    def setCounterNum(self,num):
        self.counterNum = num

    def resetImage(self, num) :
        ones = num % 10
        tens = num % 100 // 10
        hundreds = num % 1000 // 100

        print("num: %d" % (num))
        print("%d:%d:%d" % (hundreds,tens, ones))

        self.counter[0].SetBitmapLabel(imgSize(self.numSet[hundreds],26,46))
        self.counter[1].SetBitmapLabel(imgSize(self.numSet[tens],26,46))
        self.counter[2].SetBitmapLabel(imgSize(self.numSet[ones],26,46))
        self.counter[0].Refresh()
        self.counter[1].Refresh()
        self.counter[2].Refresh()

    def resetCounter(self,num):
        self.setCounterNum(num)
        self.resetImage(num)
        self.Refresh()

def main():
    app = wx.App()
    pf = wx.Frame(None)
    pc = PyCounter(pf,394)
    pc.resetCounter(12)
    pc.Refresh()
    pf.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
