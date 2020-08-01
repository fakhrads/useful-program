from pytube import YouTube
import os,subprocess,time
from moviepy.editor import *

class Youtube:

    def __init__(self):
        pass
    
    def mp3(self, url, filename="music"):
        """
        Using pytube for downloading the video and ffmpeg for converting to mp3

        Params :
            - url : youtube url (full url)
            - filename : the name of file that will saved
        """
        YouTube(url).streams.first().download(filename=filename)
        time.sleep(1)

        mp4 = "%s.mp4" % filename
        mp3 = "%s.mp3" % filename
        videoclip = VideoFileClip(mp4)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3)
        audioclip.close()
        videoclip.close()

        return(mp3)

#only for testing
yt = Youtube()
print(yt.mp3("https://www.youtube.com/watch?v=8qLL2Gx3I_k","initesting"))