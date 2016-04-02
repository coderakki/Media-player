from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon

class Gui(object):

	def __init__(self,mainwindow):
		self.mainwindow=mainwindow
	


	def setupUi(self):

		hbox = QtGui.QHBoxLayout()

		headers = "PlayList"

		self.mainwindow.videoTable = QtGui.QTreeWidget()
		self.mainwindow.videoTable.setHeaderLabel(headers)
		self.mainwindow.videoTable.itemPressed.connect(self.mainwindow.tableClicked)
		self.mainwindow.videoTable.itemDoubleClicked.connect(self.mainwindow.tableClicked)
		rightFrame = QtGui.QFrame(self.mainwindow)
		self.setup_right_frame(rightFrame)
	

		splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
		splitter.addWidget(self.mainwindow.videoTable)
		splitter.addWidget(rightFrame)

		hbox.addWidget(splitter)
		w = splitter.width()
		splitter.setSizes([w/4,3*w/4])
		widget = QtGui.QWidget()
		widget.setLayout(hbox)
	

		return widget



	def setup_right_frame(self, rightFrame):#initial right frame UI
				
		bar = QtGui.QToolBar()
		bar.addAction(self.mainwindow.playAction)
		bar.addAction(self.mainwindow.stopAction)
		bar.addAction(self.mainwindow.fullScrAction)
		bar.addAction(self.mainwindow.loopAction)
		bar.addAction(self.mainwindow.bookmarkAction)

		self.mainwindow.videoWidget.addAction(self.mainwindow.computeAction)
		self.mainwindow.videoWidget.addAction(self.mainwindow.playAction)
		self.mainwindow.videoWidget.addAction(self.mainwindow.pauseAction)

		seekSlider = Phonon.SeekSlider()
		seekSlider.Mainwindow = self.mainwindow
		seekSlider.setMediaObject(self.mainwindow.media_object)

		volumeSlider = Phonon.VolumeSlider()
		volumeSlider.setAudioOutput(self.mainwindow.audioOutput)
		volumeSlider.setSizePolicy(QtGui.QSizePolicy.Maximum, 
			QtGui.QSizePolicy.Maximum)


		self.mainwindow.timeLabel = QtGui.QLabel()
		self.mainwindow.timeLabel.setText("00:00:00")
		self.mainwindow.current_time = 0
		self.mainwindow.timeLabel.setSizePolicy(QtGui.QSizePolicy.Maximum,
			QtGui.QSizePolicy.Maximum)#this code is very important
		#it's used for fixing seekerLayout size, in order to maximum
		#videoWidget as big as possible

		seekerLayout = QtGui.QHBoxLayout()
		seekerLayout.addWidget(seekSlider)
		seekerLayout.addWidget(self.mainwindow.timeLabel)

		playbackLayout = QtGui.QHBoxLayout()
		playbackLayout.addWidget(bar)
		playbackLayout.addStretch()
		playbackLayout.addWidget(volumeSlider)

		mainLayout = QtGui.QVBoxLayout()
		mainLayout.addWidget(self.mainwindow.videoWidget)
		mainLayout.addLayout(seekerLayout)
		mainLayout.addLayout(playbackLayout)

		rightFrame.setLayout(mainLayout)

