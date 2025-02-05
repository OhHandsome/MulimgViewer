import wx
from about_gui import AboutGui
from utils import get_resource_path

class About (AboutGui):
    def __init__(self, parent):
        super().__init__(parent)

        self.about_txt.SetEditable(False)
        self.about_txt.BeginFontSize(12)
        self.about_txt.BeginBold()
        self.about_txt.WriteText("Maintainer: ")
        self.about_txt.EndBold()
        self.about_txt.WriteText("nachifur\n")

        self.about_txt.BeginBold()
        self.about_txt.WriteText("Mail: ")
        self.about_txt.EndBold()
        self.about_txt.WriteText("1476879092@qq.com\n")

        self.about_txt.BeginBold()
        self.about_txt.WriteText("Version: ")
        self.about_txt.EndBold()
        self.about_txt.WriteText("3.9.5\n")

        self.about_txt.BeginBold()
        self.about_txt.WriteText("Platform: ")
        self.about_txt.EndBold()
        self.about_txt.WriteText("python3.6\n")

        self.about_txt.BeginBold()
        self.about_txt.WriteText("Architecture: ")
        self.about_txt.EndBold()
        self.about_txt.WriteText("amd64\n")

        self.about_txt.BeginBold()
        self.about_txt.WriteText("Image format: ")
        self.about_txt.EndBold()
        self.about_txt.WriteText("png, jpg, bmp, tif\n")

        self.about_txt.BeginBold()
        self.about_txt.WriteText("Description: ")
        self.about_txt.EndBold()
        self.about_txt.WriteText(
            "MulimgViewer is a multi-image viewer that can open multiple images in one interface, which is convenient for image comparison and image stitching.\n")

        self.about_txt.EndFontSize()

        self.icon = wx.Icon(get_resource_path('mulimgviewer.ico'), wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)