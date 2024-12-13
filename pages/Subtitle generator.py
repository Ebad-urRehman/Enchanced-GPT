import whisper
import streamlit as st

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
    uploaded_file = st.file_uploader("Choose a video/audio file", type=["mp4", "mp3", "wav"])
    
    if uploaded_file is not None:
        progress_bar = st.progress(0)
        model = whisper.load_model(selected_model)
        progress_bar.progress(25)
        
        # Save the uploaded file temporarily
        file_path = f"temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        result = model.transcribe(file_path, fp16=False, task='translate')
        progress_bar.progress(75)
        st.info(result["text"])
        progress_bar.progress(100)

if selected_option == "Auto detect and Transcribe":
    uploaded_file = st.file_uploader("Choose a video/audio file", type=["mp4", "mp3", "wav"])
    
    if uploaded_file is not None:
        progress_bar = st.progress(0)
        model = whisper.load_model(selected_model)
        progress_bar.progress(25)
        
        # Save the uploaded file temporarily
        file_path = f"temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        result = model.transcribe(file_path, fp16=False)
        progress_bar.progress(75)
        st.info(result["text"])
        progress_bar.progress(100)

if selected_option == "Help":
    st.subheader("Supported Models")
    st.image("files/Whisper-help.PNG")

    st.subheader("Supported Languages")
    st.info("For help Visit https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages")
