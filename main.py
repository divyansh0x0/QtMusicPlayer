import os,sys
from audio import Audio
from window import *
from PySide6.QtCore import QRunnable, Slot, QThreadPool


MIN_DURATION = 50
def getAllAudioFiles():
    files = []
    #returns the root directory based on the os.
    #In windows it will give all drive paths while in linux the root is "/"
    roots =  getWindowsDrives() if os.name == "nt" else "/"
    
    for root in roots:
        print("visiting: ", root)
        for dirpath, dirnames, filenames in  os.walk(root,topdown=False):
            for file in filenames:
                if file.lower().endswith((".mp3",".wav",".ogg")):
                    files.append(os.path.join(dirpath,file))
    print("files found:", len(files))
    return files
def getWindowsDrives():
    return [chr(x)+":\\" for x in range(65,91) if os.path.exists(chr(x) + ":")]
def addFilesToAudioManager(audioManager):
    for file in getAllAudioFiles():
        audio = Audio(file)
        if(audio.duration > MIN_DURATION):
            audioManager.addAudio(audio)
    WINDOW.addAllAudioTiles()

    
if(__name__ == "__main__"):
    WINDOW = Window("mp3 player")
    addFilesToAudioManager(WINDOW.AUDIO_MANAGER)
    WINDOW.resize(720,600)
    WINDOW.show()
    sys.exit(WINDOW.loop())
    


