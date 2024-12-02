import wx

app = wx.App()
frame = wx.Frame(None)
panel = wx.Panel(frame)

grid_layout = wx.GridBagSizer(vgap=25, hgap=25)

button_1 = wx.Button(panel, label="Button 1")
button_2 = wx.Button(panel, label="Button 2")
button_3 = wx.Button(panel, label="Button 3")
button_4 = wx.Button(panel, label="Button 4")

grid_layout.Add(button_1, pos=(0,0), flag=wx.EXPAND)
grid_layout.Add(button_2, pos=(1,0), flag=wx.EXPAND)
grid_layout.Add(button_3, pos=(0,1), flag=wx.EXPAND)
grid_layout.Add(button_4, pos=(1,1), flag=wx.EXPAND)

grid_layout.AddGrowableCol(0)
grid_layout.AddGrowableCol(1)
grid_layout.AddGrowableCol(0)
grid_layout.AddGrowableCol(1)

panel.SetSizer(grid_layout)

frame.Show()
app.MainLoop()