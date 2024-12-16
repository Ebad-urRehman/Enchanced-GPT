import streamlit as st
from streamlit_cookies_controller import CookieController


def store_account_info():
    with st.form('Store User Account Info'):
        email = st.text_input('Email Adress(Optional : For future app updates)')
        name = st.text_input('Enter your name')
        api_key = st.text_input('Enter you API key(You can add/change this later)')

        controller = CookieController()

        submitted = st.form_submit_button('Save Info')

        if submitted:
            if email != '' and not email.endswith('@gmail.com'):
                # send email to myself to be impelemented
                pass
            

            if name != '' and api_key != '':
                controller.set('username', name)
                controller.set('apikey', api_key)
                st.success('Info submitted successfully')
            else:
                st.warning('Name and API field must not be empty')

def validate_account_info():
    controller = CookieController()

    api_key = controller.get('apikey')
    if not api_key:
        st.warning('Open AI API key is not added and most app features might not work as expected, you can add it in Check credits page')

    user_name = controller.get('username')
    
    if user_name:
        return True
    else:
        return False
    

def get_user_name():
    controller = CookieController()

    user_name = controller.get('username')

    return user_name


def get_api_key():
    controller = CookieController()

    api_key = controller.get('apikey')

    return api_key


def set_api_key(api_key):
    controller = CookieController()

    if api_key:
        controller.set('apikey', api_key)
        st.info('API Key updated successfully')

