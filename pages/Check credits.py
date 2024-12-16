import streamlit as st
from account_settings import set_api_key

# Function to get OpenAI credits
def show_openai_credits():
    url = 'https://platform.openai.com/settings/organization/usage'
    st.info(f'Check your remaining credits at {url}')


def change_api_key():
    api_key = st.text_input('Enter new API key here')

    set_api_key(api_key=api_key)


show_openai_credits()
change_api_key()
