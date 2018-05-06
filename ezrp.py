import wx
import time
import rpc
import sys

class Frame(wx.Frame):
    def __init__(self):
    	wx.Frame.__init__(self, None, title="ezrp")
    	self.Bind(wx.EVT_CLOSE, self.quit)
    	self.statusbar = self.CreateStatusBar()
    	self.statusbar.SetStatusText("Starting up...")
    	self.panel = wx.Panel(self)
    	
    	self.customState = "None"
    	self.customDetails = "None"
    	
    	self.startbutton = wx.Button(self.panel, 1, "Please wait...", wx.Point(10, 160))
    	self.startbutton.Bind(wx.EVT_BUTTON, self.toggleRunning)
    	
    	self.cfgbutton = wx.Button(self.panel, 1, "Configure", wx.Point(250, 10))
    	self.cfgbutton.Bind(wx.EVT_BUTTON, self.configureSource)
    	
    	self.dialog = wx.TextEntryDialog(self.panel, "Type in your Discord app's client ID.", "Client ID Prompt")
    	self.dialog.SetValue("442729945144229889")
    	if (self.dialog.ShowModal() == wx.ID_OK):
    		clientid = self.dialog.GetValue()
    	else:
    		self.dialog.Destroy()
    		self.quit(None)
    		sys.exit(0)
    	self.dialog.Destroy()
    	self.sourceLabel = wx.StaticText(self.panel, label="Data source:", pos=(10, 10))
    	
    	self.sourceChoice = wx.Choice(self.panel, 1, pos=(95, 10), choices=["Default Example", "Custom"])
    	
    	
    	
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
    	
    	self.rpc_obj = rpc.DiscordIpcClient.for_platform(clientid)
    def quit(self, event):
    	self.Destroy()
    def updateRp(self, event):
    	if (not updatingRp):
    		pass
    	else:
    		if (self.currentSource == "Default Example"):
    			activity = self.defExample(self.startTime)
    		if (self.currentSource == "Custom"):
    			activity = self.customData(self.startTime)
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
    def configureSource(self, event):
    	if (self.currentSource == "Default Example"):
    		dialog = wx.MessageDialog(self.panel, "The example data source does not have any configuration options.", "Error")
    		dialog.ShowModal()
    	if (self.currentSource == "Custom"):
    		dialog = wx.TextEntryDialog(self.panel, "Type in a custom state message.", "Custom Data Configuration")
    		if (dialog.ShowModal() == wx.ID_OK):
    			self.customState = dialog.GetValue()
    		dialog = wx.TextEntryDialog(self.panel, "Type in a custom details message.", "Custom Data Configuration")
    		if (dialog.ShowModal() == wx.ID_OK):
    			self.customDetails = dialog.GetValue()
    		
    def defExample(self, start_time):
    	activity = {"state": "Rich Presence Test!","details": "Powered by ezrp","timestamps": {"start": start_time}}
    	return activity
    def customData(self, start_time):
    	activity = {"state": self.customState,"details": self.customDetails,"timestamps": {"start": start_time}}
    	return activity

if (__name__ == "__main__"):
	app = wx.App(False)
	frame = Frame()
	frame.Show()
	app.MainLoop()