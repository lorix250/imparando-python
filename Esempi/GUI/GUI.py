import wx

class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, id=-1, name="Prova")
        frame.Show(True)
        button = wx.Button(parent=frame, style=wx.ID_OK, label="Il Mio Pulsante")
        return True

app = App()
app.MainLoop()