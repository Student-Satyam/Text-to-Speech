🗣️ Text-to-Speech Converter (Streamlit + gTTS)

This project is a simple and fast Text-to-Speech (TTS) web app built using Streamlit and Google Text-to-Speech (gTTS).
Users can type text, choose a language, convert the text to speech, listen to the generated MP3 audio, and download it.

🚀 Features

Convert text into speech using Google TTS

Supports English, Hindi, Spanish, French, German

Streams audio directly in the browser

Provides a downloadable MP3 file

Simple and clean Streamlit UI

Lightweight and works on Streamlit Cloud

🧩 Technologies Used

Streamlit (UI Framework)

gTTS (Google Text-to-Speech)

Python 3

📦 Installation

Install all dependencies:

pip install -r requirements.txt

▶️ Running the App

Start the Streamlit server:

streamlit run app.py


This will open the application in your web browser.

📁 Project Structure
text-to-speech/
│── app.py
│── requirements.txt
└── README.md

📝 Code Overview

Users enter text in a text box

Select a language (en, hi, es, fr, de)

Click Convert to Speech

gTTS generates an MP3 audio file in memory

Streamlit plays the audio and provides a download link

🧪 Supported Languages
Language	Code
English	en
Hindi	hi
Spanish	es
French	fr
German	de
🌐 Deploy on Streamlit Cloud

Push your project to GitHub

Visit https://streamlit.io/cloud

Select your repository

Deploy instantly — no configuration required

📄 License

This project is open-source and free to use.
