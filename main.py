import wx

app = wx.app()

icon = wx.Icon("catch!.ico")

frame = wx.Frame(None, title="Catch!")
frame.SetIcon(icon)
frame.SetBackgroundColour("#FF0000")
frame.SetSize((400, 400))
panel = wx.Panel(frame)

current_font = panel.GetFont()
current_font.SetPointSize(16)
current_font.SetUnderlined(True)
current_font.SetWeight(wx.FONTWEIGHT_BOLD)
current_font
panel.SetFont(current_font)

text = wx.StaticText(panel, label="Hello World", size=(100, 100), pos=(100, 100))
frameSetBackgroundColour("#ffce00")
frameSetForegroundColour("#ff4d00")

image = wx.StaticBitmap(panel)

frame.Center()
frame.Show()
app.MainLoop()
