from pytube import YouTube
from moviepy.editor import *

def downloadYTAudio(url, file_name):
    try:
        # Download the YouTube video
        yt = YouTube(url)
        # Get the track
        audio = yt.streams.filter(only_audio=True).first()
        # Download the audio
        audio_file = audio.download(filename="temp_audio")
        # Convert the audio to mp3
        clip = AudioFileClip(audio_file)
        clip.write_audiofile(file_name + ".mp3")
        clip.close()
        # Delete temp file
        os.remove(audio_file)
        print("Your audio file is ready!")
    except Exception as e:
        print("ERROR:", str(e))

if __name__ == "__main__":
    url = input("Enter the YouTube URL: ")
    file_name = input("Enter the name of the audio file: ")
    downloadYTAudio(url, file_name)
