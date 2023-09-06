import os
import openai
import streamlit as st

st.markdown("""
<style>
    .css-10trblm {
        text-align: center;
    }

</style>
""", unsafe_allow_html=True)
st.title("Enhanced GPT Model")

api_key = os.getenv("OPEN AI API")
dataframe = ["chat1", "chat2", "chat3"]


user_input = st.text_input("Enter Text Message here", max_chars=100, placeholder="Send a Message")