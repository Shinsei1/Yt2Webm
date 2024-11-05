import yt_dlp
import os 
from tkinter import filedialog

def download_youtube_audio(video_url):

    output_directory = filedialog.askdirectory(title="Select a folder to save your file in")
    
    os.makedirs(output_directory, exist_ok=True) 

    ydl_opts = {
        'format': 'bestaudio/best',  
        'outtmpl': os.path.join(output_directory,'%(title)s.%(ext)s'),  # Nom du fichier de sortie
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


