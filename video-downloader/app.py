from main import download_video, clean_url, get_video_info
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
buscar = st.button("🔍 Buscar video")

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

# Paso 1 — Buscar info al presionar el botón
if buscar:
    if not url:
        st.error("⚠️ Por favor ingresa una URL.")
    else:
        try:
            with st.spinner("Obteniendo información del video..."):
                st.session_state.video_info = get_video_info(url)
                st.session_state.last_url = url
        except Exception as e:
            st.error(f"❌ URL inválida o error al obtener info: {str(e)}")

# Paso 2 — Muestra info si ya fue buscada
if 'video_info' in st.session_state:
    info = st.session_state.video_info
    minutes = info['duration'] // 60
    seconds = info['duration'] % 60

    if info['thumbnail']:
        st.image(info['thumbnail'], use_container_width=True)

    st.info(f"🎬 **{info['title']}**")
    st.caption(f"⏱️ Duración: {minutes}:{seconds:02d} min")

    # Paso 3 — Botón de descarga
    if st.button("⬇️ Descargar"):
        try:
            with st.spinner("Descargando video..."):
                progress_bar = st.progress(0)
                download_video(url, progress_hook)
            st.success("✅ ¡Video descargado exitosamente!")
        except Exception as e:
            st.error(f"❌ Error al descargar: {str(e)}")





















