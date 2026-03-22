import streamlit as st
from main import download_video

st.set_page_config(
    page_title="YouTube Downloader",
    page_icon="🎥",
    layout="centered"
)

st.title("🎥 YouTube Downloader")
st.markdown("Descarga videos de YouTube en formato MP4 fácilmente.")

url = st.text_input("🔗 Pega la URL del video aquí:")

if st.button("⬇️ Descargar"):
    if not url:
        st.error("⚠️ Por favor ingresa una URL.")
    else:
        try:
            st.success("✅ ¡Video descargado exitosamente!")
