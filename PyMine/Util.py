import pathlib
import wx

def imgSize(pic,width,height):
    img = pic.ConvertToImage().Scale(width, height)   #将位图转换为图片后在改变尺寸
    bit = wx.Bitmap(img,wx.BITMAP_SCREEN_DEPTH)   #再次转换为位图
    return bit

def getImg(filename):
    # 加载图片路径，用pathlib处理不同系统下路径分隔符
    p=pathlib.PurePath("images",filename)
    # print(f"load resource: {p}")
    return str(p)

