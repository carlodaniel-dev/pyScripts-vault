from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import yt_dlp

def clean_url(url):
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    
    if 'v' not in params:
        return url
    
    clean = urlencode({'v': params['v'][0]})
    return urlunparse(parsed._replace(query=clean))

def get_video_info(url):
    ydl_opts = {
        'noplaylist': True,
        'quiet': True,        # No muestra logs en terminal
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)  # download=False, solo obtiene info
        return {
            'title': info.get('title', 'Sin título'),
            'duration': info.get('duration', 0),      # Duración en segundos
            'thumbnail': info.get('thumbnail', None),
        }

def download_video(url, progress_hook=None):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
    }

    if progress_hook:  # Solo lo agrega si se pasa uno
        ydl_opts['progress_hooks'] = [progress_hook]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])