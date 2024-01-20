from PySide6 import QtGui,QtWidgets
from PySide6.QtCore import Qt
from  datetime import timedelta

def getFormattedDuration(duration):
    #divmod returns quotient and remainder respectively
    minutes,seconds = divmod(duration,60)
    hours,minutes = divmod(minutes,60)
    hStr = str(int(hours)) + "h" if hours>0 else ""
    mStr = str(int(minutes)) + "m"if minutes > 0 else ""
    sStr = str(round(seconds)) + "s" if seconds > 0 and hStr == "" and mStr == "" else str(round(seconds))+ "s"
    return hStr+ " " + mStr + " " + sStr
     

class Tile(QtWidgets.QWidget):
    def __init__(self,audio):
        #Custom tile for displaying audios
        super().__init__()
        self.audio = audio
        self.setAutoFillBackground(True)
        colorPallete = self.palette()
        colorPallete.setColor(self.backgroundRole(),QtGui.QColor("#dddddd"))
        self.setPalette(colorPallete)
        
        layout = QtWidgets.QHBoxLayout()
        name = QtWidgets.QLabel(audio.name)
        duration = QtWidgets.QLabel(getFormattedDuration(audio.duration))
        layout.addWidget(name,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(duration,alignment=Qt.AlignmentFlag.AlignRight)
        self.setLayout(layout)