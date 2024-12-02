import wx

app = wx.App()
frame = wx.Frame(None)
panel = wx.Panel(frame)

vertical_layout = wx.BoxSizer(wx.VERTICAL)

button_1 = wx.Button(panel, label="Button 1")
button_2 = wx.Button(panel, label="Button 2")

vertical_layout.Add(button_1, proportion=1, flag=wx.ALIGN_CENTER)
vertical_layout.Add(button_2, proportion=1, flag=wx.EXPAND)

panel.SetSizer(vertical_layout)

frame.Show()
app.MainLoop()