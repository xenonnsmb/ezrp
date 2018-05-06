import wx
import time
import rpc

class Frame(wx.Frame):
    def __init__(self):
    	wx.Frame.__init__(self, None, title="ezrp")
    	self.Bind(wx.EVT_CLOSE, self.quit)
    	self.statusbar = self.CreateStatusBar()
    	self.statusbar.SetStatusText("Starting up...")
    	self.panel = wx.Panel(self)
    	
    	self.startbutton = wx.Button(self.panel, wx.ID_ANY, "Please wait...", wx.Point(10, 180))
    	self.startbutton.Bind(wx.EVT_BUTTON, self.toggleRunning)
    	
    	self.sourceLabel = wx.StaticText(self.panel, label="Data source:", pos=(10, 10))
    	
    	self.sourceChoice = wx.Choice(self.panel, wx.ID_ANY, pos=(95, 10), choices=["Default Example", "Custom"])
    	
    	self.timer = wx.Timer(self)
    	self.Bind(wx.EVT_TIMER, self.loop, self.timer)
    	self.timer.Start(1)
    	
    	self.updateTimer = wx.Timer(self)
    	self.Bind(wx.EVT_TIMER, self.updateRp, self.updateTimer)
    	self.updateTimer.Start(5000)
    	
    	self.currentSource = self.sourceChoice.GetString(self.sourceChoice.GetSelection())
    	self.lastSource = self.currentSource
    	
    	global updatingRp
    	updatingRp = False
    	
    	self.rpc_obj = rpc.DiscordIpcClient.for_platform("422523932952756234")
    def quit(self, event):
    	self.Destroy()
    def updateRp(self, event):
    	if (not updatingRp):
    		pass
    	else:
    		if (self.currentSource == "Default Example"):
    			activity = self.defExample(self.startTime)
    		self.rpc_obj.set_activity(activity)
    def loop(self, event):
    	global updatingRp
    	self.currentSource = self.sourceChoice.GetString(self.sourceChoice.GetSelection())
    	if (self.lastSource != self.currentSource):
    		updatingRp = False
    	self.lastSource = self.currentSource
    	
    	if (updatingRp):
    		self.statusbar.SetStatusText("Currently updating rich presence from source " + self.currentSource)
    		self.startbutton.SetLabel("Stop")
    	else:
    		self.statusbar.SetStatusText("Not currently running.")
    		self.startbutton.SetLabel("Start")
    def toggleRunning(self, event):
    	global updatingRp
    	updatingRp = not updatingRp
    	self.startTime = time.time()
    def defExample(self, start_time):
    	activity = {"state": "Rich Presence Test!","details": "Powered by ezrp","timestamps": {"start": start_time}}
    	return activity

app = wx.App(False)
frame = Frame()
frame.Show()
app.MainLoop()