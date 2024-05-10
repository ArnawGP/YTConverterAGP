from pytube import YouTube
from moviepy.editor import *

def DownloadAndExtract(url, fileName):
    # Download the video
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    video.download(filename='temp')

    # Extract the audio
    video_clip = AudioFileClip('temp.mp4')
    video_clip.write_audiofile(fileName)

    # Remove the temp file
    os.remove('temp.mp4')

if __name__ == "__main__":
    url = input("Introdueix la URL del vídeo de YouTube: ")
    fileName = input("Introdueix el nom de l'arxiu d'àudio de sortida (incloent l'extensió): ")

    DownloadAndExtract(url, fileName)
