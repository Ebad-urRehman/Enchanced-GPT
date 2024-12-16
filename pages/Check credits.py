import streamlit as st
import requests
import os

# Function to get OpenAI credits
def get_openai_credits(api_key):
    url = "https://api.openai.com/v1/dashboard/billing/credit_grants"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        used_credits = data['total_used']
        total_credits = data['total_granted']
        remaining_credits = total_credits - used_credits
        return used_credits, total_credits, remaining_credits
    else:
        return None, None, None

# Streamlit app layout
st.title("Remaining Credits")

# Input for OpenAI API Key
api_key = os.getenv('OPENAI_KEY')

if api_key:
    used, total, remaining = get_openai_credits(api_key)
    
    if used is not None:
        st.success(f"Total Credits: {total}")
        st.info(f"Used Credits: {used}")
        st.warning(f"Remaining Credits: {remaining}")
    else:
        st.error("Failed to retrieve credits. Check your API key or try again later.")
