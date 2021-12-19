#Boa:Frame:frm_conv

import os,time,wx,commands,sys,pexpect,subprocess,sys
import wx.lib.filebrowsebutton
import wx.stc
import wx.lib.buttons
import py2exe

ft = "(*.mp4;*.flv;*.avi)|*.mp4;*.flv;*.avi|"\
	"Semua file (*.*)|*.*|"

def create(parent):
	return frm_conv(parent)

[wxID_FRM_CONV, wxID_FRM_CONVBT_BRWSE, wxID_FRM_CONVBT_CONV, 
 wxID_FRM_CONVBT_FOLDER, wxID_FRM_CONVMOV_KONVERSI, wxID_FRM_CONVPNL_UTAMA, 
 wxID_FRM_CONVSTLX_OUTPUT, wxID_FRM_CONVSTX_FILEINP, wxID_FRM_CONVSTX_FILEOUT, 
 wxID_FRM_CONVTXC_FILEBRWSE, wxID_FRM_CONVTXC_FLDRTUJUAN, 
] = [wx.NewId() for _init_ctrls in range(11)]

class frm_conv(wx.Frame):
	
	def getpathopvar(self):
		filepathop = self.opendlg.GetPath()
		return filepathop
	
	def getfileopvar(self):
		filenameop = self.opendlg.GetFilename()
		return filenameop
	
	def setdirsavvar(self):
		dirpathsav = self.savdlg.GetPath()
		return dirpathsav

	def _init_ctrls(self, prnt):
		# generated method, don't edit
		wx.Frame.__init__(self, id=wxID_FRM_CONV, name=u'frm_conv', parent=prnt,
		      pos=wx.Point(341, 131), size=wx.Size(981, 459),
		      style=wx.DEFAULT_FRAME_STYLE, title=u'Video Ke Mp3 Konverter')
		self.SetClientSize(wx.Size(981, 459))

		self.pnl_utama = wx.Panel(id=wxID_FRM_CONVPNL_UTAMA, name=u'pnl_utama',
		      parent=self, pos=wx.Point(0, 0), size=wx.Size(981, 459),
		      style=wx.TAB_TRAVERSAL)

		self.stx_fileinp = wx.StaticText(id=wxID_FRM_CONVSTX_FILEINP,
		      label=u'File Input', name=u'stx_fileinp', parent=self.pnl_utama,
		      pos=wx.Point(32, 48), size=wx.Size(62, 17), style=0)

		self.txc_filebrwse = wx.TextCtrl(id=wxID_FRM_CONVTXC_FILEBRWSE,
		      name=u'txc_filebrwse', parent=self.pnl_utama, pos=wx.Point(136, 44),
		      size=wx.Size(696, 27), style=0, value=u'')

		self.bt_brwse = wx.Button(id=wxID_FRM_CONVBT_BRWSE, label=u'Pilih File',
		      name=u'bt_brwse', parent=self.pnl_utama, pos=wx.Point(864, 43),
		      size=wx.Size(85, 29), style=0)
		self.bt_brwse.Bind(wx.EVT_BUTTON, self.OnBt_brwseButton,
		      id=wxID_FRM_CONVBT_BRWSE)

		self.stx_fileout = wx.StaticText(id=wxID_FRM_CONVSTX_FILEOUT,
		      label=u'File Output', name=u'stx_fileout', parent=self.pnl_utama,
		      pos=wx.Point(32, 112), size=wx.Size(75, 17), style=0)

		self.txc_fldrtujuan = wx.TextCtrl(id=wxID_FRM_CONVTXC_FLDRTUJUAN,
		      name=u'txc_fldrtujuan', parent=self.pnl_utama, pos=wx.Point(136, 108),
		      size=wx.Size(696, 27), style=0, value=u'')

		self.bt_folder = wx.Button(id=wxID_FRM_CONVBT_FOLDER, label=u'Pilih Folder',
		      name=u'bt_folder', parent=self.pnl_utama, pos=wx.Point(862, 106),
		      size=wx.Size(93, 29), style=0)
		self.bt_folder.Bind(wx.EVT_BUTTON, self.OnBt_folderButton,
		      id=wxID_FRM_CONVBT_FOLDER)

		self.bt_conv = wx.Button(id=wxID_FRM_CONVBT_CONV, label=u'Konversi!',
		      name=u'bt_conv', parent=self.pnl_utama, pos=wx.Point(862, 149),
		      size=wx.Size(93, 29), style=0)
		self.bt_conv.SetBestFittingSize(wx.Size(93, 29))
		self.bt_conv.Bind(wx.EVT_BUTTON, self.OnBt_convButton,
		      id=wxID_FRM_CONVBT_CONV)

		self.mov_konversi = wx.Gauge(id=wxID_FRM_CONVMOV_KONVERSI,
		      name=u'mov_konversi', parent=self.pnl_utama, pos=wx.Point(20, 155),
		      range=100, size=wx.Size(810, 21), style=wx.GA_PROGRESSBAR)
		self.mov_konversi.SetBezelFace(1)
		self.mov_konversi.SetThemeEnabled(True)
		self.mov_konversi.SetBestFittingSize(wx.Size(810, 21))

		self.stlx_output = wx.stc.StyledTextCtrl(id=wxID_FRM_CONVSTLX_OUTPUT,
		      name=u'stlx_output', parent=self.pnl_utama, pos=wx.Point(24, 200),
		      size=wx.Size(928, 232), style=0)

	def __init__(self, parent):
		self._init_ctrls(parent)
		self.currentDirectory=os.getcwd()
		
	
	def OnBt_brwseButton(self, event):
		self.opendlg = wx.FileDialog(self, "Pilih File", ".", "", ft,wx.OPEN)
		try:
			if self.opendlg.ShowModal()==wx.ID_OK:
				self.txc_filebrwse.SetValue(self.getfileopvar())
		finally:
			self.opendlg.Hide()

	def OnBt_folderButton(self, event):
		self.savdlg = wx.FileDialog(self, "Pilih Folder", ".", "", ".mp3",wx.SAVE)
		
		try:
			if self.savdlg.ShowModal()==wx.ID_OK:
				self.txc_fldrtujuan.SetValue(self.setdirsavvar()+".mp3")
		finally:
			self.savdlg.Hide()
		
		#self.savdlg = wx.DirDialog(self, "Pilih Folder", self.currentDirectory, wx.OK)
		#try:
		#	if self.savdlg.ShowModal()==wx.ID_OK:
		#		self.txc_fldrtujuan.SetValue(self.setdirsavvar())
		#finally:
		#	self.savdlg.Hide()

	def OnBt_convButton(self, event):
		self.stlx_output.AddText("\n")
		self.stlx_output.AddText("Memulai Konversi . . .\n")
		
		exe = ["ffmpeg","-i",""+self.getpathopvar()+"",""+self.setdirsavvar()+".mp3"]
		
		count = 0		

		proc = subprocess.Popen(exe,
					stdout=subprocess.PIPE,
					stderr=subprocess.STDOUT)				
		
		while count < 101:
			wx.Yield()
			self.mov_konversi.SetValue(count)
			self.bt_conv.Disable()
			self.stlx_output.AddText("|")
			for line in proc.stdout:
				self.stlx_output.AddText(""+line.rstrip())
				self.stlx_output.AddText("\n")
			time.sleep(0.5)
			count+=1
		self.psn = wx.MessageDialog(self,"Konversi Selesai","Info",wx.OK)
		self.psn.ShowModal()
		self.bt_conv.Enable()
		
		#self.mov_konversi.SetRange(os.path.getsize(self.getpathopvar()))
		#count = 0
		#while count < self.mov_konversi.GetRange():
		#	wx.Yield()
		#	self.mov_konversi.SetValue(count)
		#	self.bt_conv.Disable()
		#	self.stlx_output.AppendText("|")
		#	count+=1
		#time.sleep(3)
		
		#self.stlx_output.AppendText("\nKonversi Selesai!")
		#size = os.path.getsize(self.getpathopvar())
		#
		#self.mov_konversi.SetRange(size)
		#count = 0
		#while count < self.mov_konversi.GetRange():
		#	wx.Yield()
		#	self.mov_konversi.SetValue(count)
		#	self.bt_conv.Disable()
		#	count+=5
		#
		#self.bt_conv.Enable()
		#
		
		#conv = os.system("ffmpeg -i "+self.getpathopvar()+" "+self.setdirsavvar()+"/coba.mp3")
		
		
		#out = commands
		
		#os.system("ffmpeg -i "+self.getpathopvar()+" "+self.setdirsavvar()+"/coba.mp3 2>"+self.setdirsavvar()+"/coba_log.txt")
		
		#self.stlx_output.LoadFile(self.setdirsavvar()+"/coba_log.txt")
		#hsl=out.getstatusoutput("ffmpeg -i "+self.getpathopvar()+" "+self.setdirsavvar()+"/coba.mp3")
		#self.stlx_output.AppendText(hsl)
		
		#convex = "ffmpeg -i "+self.getpathopvar()+" "+self.setdirsavvar()+"/coba.mp3"
		#thread = pexpect.spawn(convex)
		#cpl = thread.compile_pattern_list([
		#	pexpect.EOF,
		#	"frame= *\d+",
		#	'(.+)'
		#])
		#while True
		#	i = thread.expect_list(cpl, timeout=None)
		#	if i == 0:
		#		self.stlx_output.AppendText("\nKonversi selesai!")
		#		break+
		#	elif i == 1:
		#		frame_num = thread.match.group(0)
		#		print frame_num
		#		thread.close
		#	elif i == 2:
		#		pass
		
		
		#self.psn = wx.MessageDialog(self,"Di Co Ba!!!","maho",wx.OK)
		#self.psn.ShowModal()
		
		#os.system("ffmpeg -i "+self.getpathopvar()+" "+self.setdirsavvar()+"/coba.mp3")
