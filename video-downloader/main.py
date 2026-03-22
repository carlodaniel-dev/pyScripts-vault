import yt_dlp as yt_dlp
import yt_dlp

def download_YT(urls):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,       # Solo descarga el video, ignora la playlist
        'playlist_items': '1',    # Por si acaso, solo toma el primer item
        'noprogress': False,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

# Lista de URLs de videos de YouTube a descargar
video_urls = [
    "https://www.youtube.com/watch?v=KxbRTLwZVKE&list=RDKxbRTLwZVKE&start_radio=1"
]

download_YT(video_urls)
print("✅ Descarga completada!")