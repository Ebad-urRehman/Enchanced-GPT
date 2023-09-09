import os
import openai
import streamlit as st
import functions
import time
import pandas as pd

current_time = time.localtime()

# i is denoting no of responses here
i = 0

day = time.strftime("%d", current_time)
month = time.strftime("%B", current_time)
year = time.strftime("%Y", current_time)
if os.path.exists("files/account.json"):
    f_name, l_name, email_ad, dob = functions.sign_up()
    print(f"{f_name} {l_name} {email_ad} {dob}")
    account_dataframe = [
        {
            "firstname": f"{f_name}",
            "lastname": f"{l_name}",
            "fullname": f"{f_name}{l_name}",
            "mail": f"{email_ad}",
            "dob": f"{dob}"
        }
    ]
else:
    st.markdown("""
    <style>
        .css-10trblm {
            text-align: center;
        }
    
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"<p style='text-align: right;'>{day} : {month} : {year}</p>", unsafe_allow_html=True)
    st.title("Enhanced GPT Model")

# st.markdown(f"""
# <style>
# .stTextArea{{
#         position: fixed;
#         bottom: 0;
#         z-index: 3;
#         line-height: 9.6;
#         padding-bottom: 9rem;
#         caret-color: rgb(250, 250, 250);
#         color: rgb(250, 250, 250);
#         border:0px solid white;
#         border-right: 2px solid #000
#         padding: 0px;
#         max-height: 100px;
#         }}
#     </style>
# """, unsafe_allow_html=True)
#
# user_input = ""
# user_input = st.text_area("", placeholder="Send a Message")
#
# st.markdown(f"""
# <style>
# .text_area1{{
#         position: fixed;
#         bottom: 1;
#         z-index: 3;
#         line-height: 9.6;
#         padding-bottom: 9rem;
#         caret-color: rgb(250, 250, 250);
#         color: rgb(250, 250, 250);
#         border:0px solid white;
#         border-right: 2px solid #000
#         padding: 0px;
#         max-height: 100px;
#         }}
#     </style>
# """, unsafe_allow_html=True)
# #
# # user_input = ""
# st.text_area("", placeholder="Send a Message", key="text_area1")

chat_default_text = "&#x25CF Aslam u Alaikum!<br> &#x25CF I am Enhanced GPT<br> &#x25CF Write a Text and get an Answer Record a Question and get an Answer<br> &#x25CF I can read these Answers for you<br>"

if i == 0:
    typewriter_chat_default = functions.typewriter_text(chat_default_text)
    st.markdown(typewriter_chat_default, unsafe_allow_html=True)
    user_input = ""

while True:
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

    user_input = st.text_area("", placeholder="Send a Message", key=f".stTextArea{i}")
    if user_input != "":
        formatted_time = time.strftime("%I:%M %p", current_time)

        st.markdown(f"""User""", unsafe_allow_html=True)
        typewriter_user_input = functions.typewriter_text(user_input)
        st.markdown(typewriter_user_input, unsafe_allow_html=True)
        # Right-align text using HTML
        layout = []
        layout.append(f"<p style='text-align: right;'>{formatted_time}</p>")
        st.markdown(f"{layout[0]}", unsafe_allow_html=True)

        chat = functions.Chatbot()


        chat_response = chat.get_response(user_input)
        typewriter_response = functions.typewriter_text(chat_response)
        st.markdown("""Enhanced GPT""")
        st.markdown(typewriter_response, unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: right;'>{formatted_time}</p>", unsafe_allow_html=True)

        history_dataframe = []
        if i == 1:
            history_dataframe = [{
                f"time{i}": f"{formatted_time}",
                f"date{i}": f"{day} : {month} : {year}",
                f"response_no{i}": i
            }]
        else:
            history_dataframe.append({
                    f"time{i}": f"{formatted_time}",
                    f"date{i}": f"{day} : {month} : {year}",
                    f"response_no{i}": i
                })
        if i==3:
            break
        i = i + 1
        print(history_dataframe)
