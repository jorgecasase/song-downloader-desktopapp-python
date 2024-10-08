import os
from yt_dlp import YoutubeDL
import sys

ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg', 'ffmpeg.exe')
ffmpeg_path = os.path.join(sys._MEIPASS, 'ffmpeg', 'ffmpeg.exe')

def descargar_audio(url, download_dir):

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '320',
        }],
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'ffmpeg_location': ffmpeg_path
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        title = info_dict.get('title')

    return title

