import yt_dlp
import os 

def download_youtube_audio(video_url):
    # Options pour le téléchargement

    output_directory = "C:\\audios\\"  
    os.makedirs(output_directory, exist_ok=True) 

    ydl_opts = {
        'format': 'bestaudio/best',  
        'outtmpl': os.path.join(output_directory,'%(title)s.%(ext)s'),  # Nom du fichier de sortie
    }

    # Téléchargement avec yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

#Exemple 
#video_url = 'https://www.youtube.com/watch?v=2zdnd2PD_l0&list=LL&index=2'  
#download_youtube_audio(video_url)
