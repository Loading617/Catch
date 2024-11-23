   import wx

   class MyFrame(wx.Frame):
       def __init__(self, parent, title):
           super(MyFrame, self).__init__(parent, title=title)

           self.SetSize(self.FromDIP(wx.Size(400, 300)))
           self.panel = wx.Panel(self)

           self.text = wxStaticText(self.panel, label="Hello, wxPython!")

           self.Show(True)
           
class MyApp(wx.App):
   def OnInit(self):
       frame = MyFrame(None, "My wxPython App")
       frame.Show()
       return True

   if __name__ == "__main__":
       app = MyApp()
       app.MainLoop()
