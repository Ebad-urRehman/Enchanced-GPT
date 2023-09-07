import os
import openai
import streamlit as st
import functions


if not os.path.exists("files/account.txt"):
    f_name, l_name, email_ad, dob = functions.sign_up()
    print(f"{f_name} {l_name} {email_ad} {dob}")

else:
    st.markdown("""
    <style>
        .css-10trblm {
            text-align: center;
        }
    
    </style>
    """, unsafe_allow_html=True)
    st.title("Enhanced GPT Model")

    dataframe = ["chat1", "chat2", "chat3"]



user_input = functions.input_at_bottom()
st.markdown(user_input, unsafe_allow_html=True)

chat_default_text = "&#x25CF Aslam u Alaikum!<br> &#x25CF I am Enhanced GPT<br> &#x25CF Write a Text and get an Answer Record a Question and get an Answer<br> &#x25CF I can read these Answers for you<br>"

typewriter_chat_default = functions.typewriter_text(chat_default_text)
st.markdown(typewriter_chat_default, unsafe_allow_html=True)


chat = functions.Chatbot()

chat_response = chat.get_response(user_input)

typewriter_response = functions.typewriter_text(chat_response)
st.markdown(typewriter_response, unsafe_allow_html=True)