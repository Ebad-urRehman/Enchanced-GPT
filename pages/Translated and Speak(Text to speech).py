import streamlit as st
import functions
from pydub import AudioSegment
from pydub.playback import play

st.header("Translated Text to speech")

# creating input box styling
st.markdown(f"""
<style>
.stTextArea{{
        position: fixed;
        bottom: 0;
        z-index: 3;
        line-height: 9.6;
        padding-bottom: 9rem;
        caret-color: rgb(250, 250, 250);
        color: rgb(250, 250, 250);
        border:0px solid white;
        border-right: 2px solid #000
        padding: 0px;
        max-height: 100px;
        }}
    </style>
""", unsafe_allow_html=True)
# text area input
text = st.text_area("", placeholder="Send a Message")
# making tts class

tts_object = functions.TextToSpeech()

lang_dict = tts_object.get_lang_dict()
lang_list = lang_dict.keys()

input_lang_choice = st.selectbox("Select Input Language", lang_list)
output_lang_choice = st.selectbox("Select Output Language", lang_list)

# extracting language name according to choice(ur for urdu)
input_lang = lang_dict[input_lang_choice]
output_lang = lang_dict[output_lang_choice]
st.info(f"{input_lang}, {output_lang}")

mode = st.radio("Select mode", ["Slow", "Fast"])
if mode == "Slow":
    selection = True
else:
    selection = False

if text:
    if input_lang == output_lang:
        tts_object.text_to_speech(text, output_lang, mode)
    else:
        translated_text = tts_object.trans(text, input_lang, output_lang)
        st.info(f"Translated Text : {translated_text}")
        tts_object.text_to_speech(translated_text, output_lang, mode)

