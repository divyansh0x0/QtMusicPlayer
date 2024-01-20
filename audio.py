import os,playsound, audio_metadata
class Audio:
    def __init__(self, path):
        self.path = path
        self.duration = 0
        self.name = os.path.basename(path)
        try:
            data = audio_metadata.load(path)
            self.duration = float(data.streaminfo["duration"])
            self.name = data.tags["title"][0]
        except:
            pass                
    

    
 