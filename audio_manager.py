from audio import Audio
from pygame import mixer
class AudioManager():
    def __init__(self):
        super().__init__()
        self.queue = []
        self.currAudioIndex = 0
        self.errorOccurred = lambda e : print(e)
        self.isPaused = True
        self.playbackStateChanged = None
        self.player = mixer.music
        mixer.init()
        
    def addAudio(self,audio):
       self.queue.append(audio) if isinstance(audio,Audio) else print(audio,"is not an audio")    
    def getAudios(self):
        return self.queue
    def getCurrAudio(self):
        return self.queue[self.currAudioIndex]
    
    def playAudio(self,audio):
        self.currAudioIndex = self.queue.index(audio)
        self.player.stop()
        self.player.load(audio.path)
        self.player.play()
        
        self.isPaused = False
        if(self.playbackStateChanged != None):
            self.playbackStateChanged()
        print("playing: " + audio.path)
            
    def playPrevAudio(self):
        prevIndex = self.currAudioIndex - 1 if self.currAudioIndex > 0 else 0
        if(not self.isPaused):
            self.playAudio(self.queue[prevIndex])
        else:
            self.currAudioIndex = prevIndex
    def playNextAudio(self):
        nextIndex  = self.currAudioIndex + 1 if self.currAudioIndex < (len(self.queue)-1) else 0
        if(not self.isPaused):
            self.playAudio(self.queue[nextIndex])
        else:
            self.currAudioIndex = nextIndex
    
    def playPauseAudio(self):
        if(len(self.queue)>0 and self.isPaused):
            self.playAudio(self.queue[self.currAudioIndex])
        else:
            self.pause()
    def pause(self):
        self.isPaused = True
        self.player.pause()
        
        if(self.playbackStateChanged != None):
            self.playbackStateChanged()
    
        
    
    