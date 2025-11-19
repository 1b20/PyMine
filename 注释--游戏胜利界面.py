from datetime import time

import wx
import threading
import threading as thread

class Singleton(object):#单例模式基类，确保只有一个实例
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class WinFrame(wx.Frame, Singleton):
    """
    游戏胜利界面窗口类
    职责：显示游戏胜利信息并提供难度选择和重启功能
    设计意图：作为扫雷游戏胜利后的交互界面，采用单例模式确保唯一性
    使用方法：通过Show()方法显示，通过按钮事件与主游戏交互
    """
    def __init__(self, parent, style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX) | wx.STAY_ON_TOP,
                 *args, **kw):
        """创建胜利面板
        参数:
            parent: 父窗口
            style: 窗口样式，默认去掉了调整大小和最大化按钮，并置顶显示
        """
        # 调用父类构造函数
        wx.Frame.__init__(self, parent,style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX) | wx.STAY_ON_TOP, *args,**kw)

        self.parent = parent  # 保存父窗口引用

        self.mineCount = 0  # 地雷数量

        self.winTimer = WinTimer()  # 创建胜利计时器

        # 创建界面组件
        # 创建祝贺文本
        msg = wx.StaticText(self, 1, "  Congratulation!  ", wx.Point(15, 30))
        msg1 = wx.StaticText(self, 2, "   You win.   ", wx.Point(15, 30))
        msg2 = wx.StaticText(self, 3, "  Click to restart!  ", wx.Point(15, 30))

        # 创建难度选择按钮
        easy = wx.Button(self, label="Easy")
        easy.Bind(wx.EVT_BUTTON, self.OnEasyButtonClicked)

        middle = wx.Button(self, label="Middle")
        middle.Bind(wx.EVT_BUTTON, self.OnMiddleButtonClicked)

        hard = wx.Button(self, label="Hard")
        hard.Bind(wx.EVT_BUTTON, self.OnHardButtonClicked)

        # 创建关闭按钮
        self.closeBtn = wx.Button(self, label="Close")
        self.closeBtn.Bind(wx.EVT_BUTTON, self.OnCloseButtonClicked)

        # 绑定窗口关闭事件
        self.Bind(wx.EVT_CLOSE, self.close)

        # 创建布局管理器
        Sizer = wx.BoxSizer(wx.VERTICAL)  # 垂直布局

        # 添加组件到布局
        Sizer.Add(msg)
        Sizer.Add(msg1)
        Sizer.Add(msg2)
        Sizer.Add(easy)
        Sizer.Add(middle)
        Sizer.Add(hard)
        Sizer.Add(self.closeBtn)

        # 应用布局
        self.SetSizerAndFit(Sizer)

    def getMineNum(self):
        """
        获取基于难度级别计算的地雷数量
        业务逻辑：难度级别与地雷数成正比关系，每级增加12个地雷
        返回值：地雷数量（初级12，中级24，高级36）
        """
        return (self.level * 12)

    def getWinOk(self):#获取窗口状态标志
        return self.isOk

    def setWinOk(self, flag):#设置窗口状态标志
        self.isOk = flag

    def close(self, event=None):#关闭应用程序
        self.parent.Close()

    def Stop(self):#停止胜利界面
        if self.getWinOk() == True:
            self.setWinOk(False)

    def Start(self):#启动胜利界面
        if self.getWinOk() == False:
            self.setWinOk(True)

    def Ready(self):#准备胜利界面
        self.setWinOk(False)

    def OnEasyButtonClicked(self, e):
        """
        初级难度按钮点击事件处理
        业务逻辑：设置初级难度参数并通知主游戏重新开始
        执行流程：停止当前界面→设置参数→通知主游戏→隐藏界面
        """
        self.Stop()  # 停止当前界面
        self.mineCount = 12  # 设置地雷数
        self.level = 1  # 设置难度级别
        self.parent.setNewGame(self.mineCount)  # 通知父窗口开始新游戏
        self.setWinOk(True)  # 设置状态
        self.parent.timer.Stop()  # 停止父窗口计时器
        self.Hide()  # 隐藏胜利窗口
        e.Skip()  # 继续事件处理

    def OnMiddleButtonClicked(self, e):#中级难度按钮点击事件
        self.Stop()
        self.mineCount = 24
        self.level = 2
        self.parent.setNewGame(self.mineCount)
        self.setWinOk(True)
        self.parent.timer.Stop()
        self.Hide()
        e.Skip()

    def OnHardButtonClicked(self, e):#高级难度按钮点击事件
        self.Stop()
        self.mineCount = 36
        self.level = 3
        self.parent.setNewGame(self.mineCount)
        self.setWinOk(True)
        self.parent.timer.Stop()
        self.Hide()
        e.Skip()

    def OnCloseButtonClicked(self, e):#关闭按钮点击事件
        self.close()

    def getMineNum(self):#获取地雷数量
        return self.mineCount


class WinTimer(threading.Thread, Singleton):
    """
    胜利界面计时器线程类
    职责：在胜利界面显示时运行后台计时任务
    设计意图：采用单例模式确保计时器唯一性，避免多个计时器冲突
    """
    def __init__(self):#初始化计时器线程
        threading.Thread.__init__(self, group=None)
        self.start()  #线程创建后立即启动

    def run(self):#线程执行的主函数
        try:
            while (self.getWinOk() == True):  # 循环检查状态
                self.acquire()  # 获取锁
                time.sleep(1) # 休眠1秒
                print("zbzbzb")
                self.release()  # 释放锁
        except:
            print("error")  # 异常处理过于简单


if __name__ == '__main__':# 测试代码
    app = wx.App()
    frame = WinFrame(None, title="You win")
    frame.Size = (300, 200)
    frame.Show()

    app.MainLoop()
