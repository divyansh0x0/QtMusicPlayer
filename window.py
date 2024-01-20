from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import *
from tile import Tile
import audio_manager,audio
from PySide6.QtMultimedia import *

class Window(QtWidgets.QWidget):
    AUDIO_MANAGER = audio_manager.AudioManager()
    def __init__(self,title):
        self.app = QtWidgets.QApplication([])
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle(title)
        self.setMinimumSize(600,400)
        self.root = QtWidgets.QVBoxLayout(self)

        #label to show some state informations
        self.infoLabel = QtWidgets.QLabel()
        self.infoLabel.setText("Hi")

        #tile container
        self.tileContainer = QtWidgets.QVBoxLayout()
        groupBox = QtWidgets.QGroupBox()
        groupBox.setLayout(self.tileContainer)
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidget(groupBox)
        self.scrollArea.setWidgetResizable(True)

        #layout control buttons
        self.buttonLayout = QtWidgets.QHBoxLayout()
        btnGroupBox = QtWidgets.QGroupBox()
        btnGroupBox.setLayout(self.buttonLayout)
        #control buttons
        self.playBtn = QtWidgets.QPushButton("Play")
        self.playBtn.clicked.connect(lambda e:self.AUDIO_MANAGER.playPauseAudio())
        self.prevBtn = QtWidgets.QPushButton("Prev")
        self.prevBtn.clicked.connect(lambda e: self.AUDIO_MANAGER.playPrevAudio())
        self.nextBtn = QtWidgets.QPushButton("Next")
        self.nextBtn.clicked.connect(lambda e: self.AUDIO_MANAGER.playNextAudio())
        
        # self.positionSlider = QtWidgets.QSlider()
        #adding components
        self.root.addWidget(self.infoLabel,alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.root.addWidget(self.scrollArea,stretch=1)
        
        bottomCenterAlign = Qt.AlignmentFlag.AlignBottom |Qt.AlignmentFlag.AlignLeft
        self.buttonLayout.addWidget(self.playBtn,alignment=bottomCenterAlign)
        self.buttonLayout.addWidget(self.prevBtn,alignment=bottomCenterAlign)
        self.buttonLayout.addWidget(self.nextBtn,alignment=bottomCenterAlign)
        
        self.root.addWidget(btnGroupBox,alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        
        self.AUDIO_MANAGER.playbackStateChanged =  self.handleMediaStateChange
        # self.AUDIO_MANAGER.playbackStateChanged.connect(self.handleMediaStateChange)
   
    def handleMediaStateChange(self):
        if self.AUDIO_MANAGER.isPaused: 
            self.playBtn.setText("Play")
            self.setInfoText("playback paused")
        else:
            self.playBtn.setText("Pause")
            self.setInfoText("Playing: " + self.AUDIO_MANAGER.getCurrAudio().path)
        
    def setInfoText(self,infoText):
        self.infoLabel.setText(infoText)
    
    def addAllAudioTiles(self):
        for audio in  self.AUDIO_MANAGER.getAudios():
            self.addAudioTile(audio)
    def addAudioTile(self,audio:audio.Audio):
        tile = Tile(audio)
        tile.setMinimumWidth(100)
        tile.setMinimumHeight(100)
        tile.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,QtWidgets.QSizePolicy.Policy.Preferred)
        tile.mouseReleaseEvent = lambda event : self.AUDIO_MANAGER.playAudio(tile.audio)
        self.tileContainer.addWidget(tile)
    
        
    def loop(self):
        return self.app.exec()

    
                
