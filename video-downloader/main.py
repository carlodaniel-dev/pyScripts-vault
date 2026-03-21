import yt_dlp as yt_dlp

def download_YT(urls):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls) 

# Lista de URLs de videos de YouTube a descargar
video_urls = [
    "https://www.youtube.com/watch?v=VIDEO_ID1",
    "https://www.youtube.com/watch?v=VIDEO_ID2",
    "https://www.youtube.com/watch?v=VIDEO_ID3"
]

download_YT(video_urls)