from main import download_video, clean_url
import streamlit as st
import re

st.set_page_config(
    page_title="YouTube Downloader",
    page_icon="🎥",
    layout="centered"
)

st.title("🎥 YouTube Downloader")
st.markdown("Descarga videos de YouTube en formato MP4 fácilmente.")

url = st.text_input("🔗 Pega la URL del video aquí:")

# Función para validar la URL de YouTube
def is_valid_youtube_url(url):
    pattern = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[a-zA-Z0-9_-]{11}'
    return bool(re.match(pattern, url))

# Función para actualizar la barra de progreso
def progress_hook(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
        downloaded = d.get('downloaded_bytes', 0)
        if total > 0:
            percent = int((downloaded / total) * 100)
            progress_bar.progress(percent)
    elif d['status'] == 'finished':
        progress_bar.progress(100)


# Botón para iniciar la descarga
if st.button("⬇️ Descargar"):
    if not url:
        st.error("⚠️ Por favor ingresa una URL.")
    elif not is_valid_youtube_url(url):  
        st.error("⚠️ La URL no es válida. Asegúrate de que sea un enlace de YouTube.")
    else:
        try:
            with st.spinner("Descargando video..."):
                progress_bar = st.progress(0)       # Se crea aquí cuando se necesita
                url = clean_url(url)                # Limpia la URL antes de descargar
                download_video(url, progress_hook)  # Solo la instanciamos

            st.success("✅ ¡Video descargado exitosamente!")

        except Exception as e:
            st.error(f"❌ Error al descargar: {str(e)}")