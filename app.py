
import streamlit as st
from gtts import gTTS
import io
import base64

st.set_page_config(page_title="Text-to-Speech Converter", layout="centered")
st.title("Text-to-Speech Converter by sattu")

# Text input for the user
user_text = st.text_area("Enter text here:", "Hello, how are you today?", height=200)

# Language selection
language = st.selectbox("Select Language", ['en', 'hi', 'es', 'fr', 'de'], index=0)

if st.button("Convert to Speech"):
    if user_text:
        try:
            # Generate speech using gTTS
            tts = gTTS(text=user_text, lang=language)
            
            # Save to an in-memory byte stream
            audio_bytes_io = io.BytesIO()
            tts.write_to_fp(audio_bytes_io)
            audio_bytes_io.seek(0)

            st.success("Speech generated successfully!")
            
            # Display an audio player
            st.audio(audio_bytes_io.read(), format='audio/mp3', start_time=0)

            # Create download link
            # Re-read the BytesIO object as st.audio might consume it
            audio_bytes_io.seek(0)
            b64 = base64.b64encode(audio_bytes_io.getvalue()).decode()
            href = f'<a href="data:audio/mp3;base64,{b64}" download="output.mp3">Click here to download the audio file!</a>'
            st.markdown(href, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"An error occurred during speech generation: {e}")
    else:
        st.warning("Please enter some text to convert.")
