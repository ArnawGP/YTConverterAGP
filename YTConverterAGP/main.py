from pytube import YouTube
from moviepy.editor import *

def descarregar_audio_des_de_youtube(url, nom_arxiu):
    try:
        # Descarregar el vídeo
        yt = YouTube(url)
        # Obtenir la millor pista d'àudio
        audio = yt.streams.filter(only_audio=True).first()
        # Descarregar l'àudio
        audio_file = audio.download(filename="temp_audio")
        # Convertir l'àudio a MP3
        clip = AudioFileClip(audio_file)
        clip.write_audiofile(nom_arxiu + ".mp3")
        clip.close()
        # Eliminar l'arxiu temporal
        os.remove(audio_file)
        print("S'ha descarregat l'àudio com a MP3 amb èxit!")
    except Exception as e:
        print("Hi ha hagut un error:", str(e))

if __name__ == "__main__":
    url = input("Introdueix la URL del vídeo de YouTube: ")
    nom_arxiu = input("Introdueix el nom per a l'arxiu d'àudio: ")
    descarregar_audio_des_de_youtube(url, nom_arxiu)
