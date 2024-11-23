   import wx

   class MyFrame(wx.Frame):
       def __init__(self, parent, title):
           super().__init__(parent, title=title, size=(300, 200))
           self.panel = wx.Panel(self)
           self.button = wx.Button(self.panel, label="Click me")
           self.button.Bind(wx.EVT_BUTTON, self.on_click)

       def on_click(self, event):
           wx.MessageBox("Hello from wxPython!", "Message", wx.OK | wx.ICON_INFORMATION)

   if __name__ == '__main__':
       app = wx.App()
       frame = MyFrame(None, "My wxPython App")
       frame.Show()
       app.MainLoop()
