import streamlit as st
import os
from tts_utils import text_to_speech, increase_speed

st.set_page_config(page_title="Text to Audio", layout="wide")

st.title("🎙️ Text to Audio Converter")
st.markdown("Convert text to speech with adjustable speed!")

# Big text input area
text = st.text_area("✍️ Enter text", height=400)
file_name = st.text_input("📁 Output File Name (without extension)", value="output")
playback_speed = st.slider("⏩ Playback Speed", min_value=0.5, max_value=2.0, value=1.05, step=0.05)

if st.button("🎧 Convert to Audio"):
    if not text.strip():
        st.warning("Please enter some Hindi text.")
    else:
        base_file =  f"{file_name}.mp3"
        final_file = f"{file_name}.mp3"

        with st.spinner("Converting..."):
            text_to_speech(text, base_file)
            increase_speed(base_file, speed=playback_speed, output_file=final_file)

        st.success("✅ Audio conversion complete!")
        st.audio(final_file)
        
        with open(final_file, "rb") as f:
            st.download_button("⬇️ Download Audio", f, file_name=final_file, mime="audio/mp3")

        # Optional cleanup
        if os.path.exists(base_file):
            os.remove(base_file)
