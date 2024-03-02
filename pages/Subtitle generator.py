import whisper
import streamlit as st

import wx

app = wx.App(None)

st.header("▶🎥Audio/Video Subtitle generator")
st.info("""🌐Browse for a audio/video file to generate its subtitle\n
➡Translate any Language Subtitles into English\n
📜Transcribe any Language Subtitles\n
🤖Whisper Openai Model""")

options = ["Transcribe and Translate", "Auto detect and Transcribe", "Help"]
selected_option = st.sidebar.radio("Select mode", options)

models = ["Tiny", "Base", "Small", "Medium", "Large"]
selected_model = st.sidebar.selectbox("Select Model", models)
for model in models:
    if selected_model == model:
        selected_model = model.lower()
st.info(selected_model)
if selected_option == "Transcribe and Translate":
    if st.button("Browse"):
        wildcard = "MP4 files (*.mp4)|*.mp4|MP3 files (*.mp3)|*.mp3|WAV files (*.wav)|*.wav"
        dialog = wx.FileDialog(None, "Select a video/audio file:", wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dialog.ShowModal() == wx.ID_OK:
            file_path = dialog.GetPath()

        if file_path:
            progress_bar = st.progress(0)
            model = whisper.load_model(selected_model)
            progress_bar.progress(25)
            result = model.transcribe(file_path, fp16=False, task='translate')
            progress_bar.progress(75)
            st.info(result["text"])
            progress_bar.progress(100)

if selected_option == "Auto detect and Transcribe":
    if st.button("Browse"):
        wildcard = "MP4 files (*.mp4)|*.mp4|MP3 files (*.mp3)|*.mp3|WAV files (*.wav)|*.wav"
        dialog = wx.FileDialog(None, "Select a video/audio file:", wildcard=wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dialog.ShowModal() == wx.ID_OK:
            file_path = dialog.GetPath()

        # audio uploader
        if file_path:
            progress_bar = st.progress(0)
            model = whisper.load_model(selected_model)
            progress_bar.progress(25)
            result = model.transcribe(file_path, fp16=False)
            progress_bar.progress(75)
            st.info(result["text"])
            progress_bar.progress(100)

if selected_option == "Help":
    st.subheader("Supported Models")
    st.image("files/Whisper-help.PNG")

    st.subheader("Supported Languages")
    st.info("For help Visit https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages")

