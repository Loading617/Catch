import wx
from utils import ensure_hdpi
class MyFrame(wx.Frame):
       def __init__(self, parent, title):
           super(MyFrame, self).__init__(parent, title=title)

           self.SetSize(self.FromDIP(wx.Size(400, 300)))
           self.panel = wx.Panel(self)

           self.fileContents = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
           self.button = wx.Button(self.panel, label="Open File")

           self.text = wxStaticText(self.panel, label="Hello, wxPython!")


           self.Bind(wx.EVT_BUTTON, self.on_click, self.button)

           self.sizer = wx.BoxSizer(wx.VERTICAL)
           self.sizer.Add(self.fileContents, 1, wx.EXPAND)
           self.sizer.Add(self.button, 0, wx.ALIGN_CENTER | wx.ALL, self.FromDIP(10))
           self.sizer.AddStretchSpacer()

           self.panel.SetSizer(self.sizer)

           self.Show(True)
           
        def OnButtonClick(self, event):
            dialog = wx.FileDialog(self, "Open File", style=wx.FD_OPEN | wx.FILE_MUST_EXIST
                                   wildcard= "Video files (*.mp4)|*.mp4")
            if dialog.ShowModal() == wx.ID_OK:
               wx.MessageBox("Success", "Info", wx.OK)    
                try:
                    with open(dialog.GetPath()), 'r') as file:
                        self.fileContents.SetValue(file.read())
            except Exception as e:
                wx.MessageBox(str(e), "Error", wx.OK | wx.ICON_ERROR)
            
class MyApp(wx.App):
   def OnInit(self):
       
       ensure_hdpi()

       frame = MyFrame(None, "My wxPython App")
       frame.Show()
       return True

   if __name__ == "__main__":
       app = MyApp()
       app.MainLoop()
