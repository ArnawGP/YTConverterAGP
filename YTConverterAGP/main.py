from pytube import YouTube
from moviepy.editor import *

def descarregar_i_extreure_audio(url, nom_arxiu):
    # Descarregar el vídeo de YouTube
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    video.download(filename='temp')

    # Extreure l'àudio del vídeo
    video_clip = AudioFileClip('temp.mp4')
    video_clip.write_audiofile(nom_arxiu)

    # Eliminar el vídeo temporal
    os.remove('temp.mp4')

if __name__ == "__main__":
    url = input("Introdueix la URL del vídeo de YouTube: ")
    nom_arxiu = input("Introdueix el nom de l'arxiu d'àudio de sortida (incloent l'extensió): ")

    descarregar_i_extreure_audio(url, nom_arxiu)
