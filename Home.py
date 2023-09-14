import os
import openai
import streamlit as st
import functions
import time
import json
import glob
# i is denoting no of responses here
i = 0
if 'current_page_responses' not in st.session_state:
    st.session_state.current_page_responses = []

if 'time_list' not in st.session_state:
    st.session_state.time_list = []
# History data frame to keep track of older responses and storing them in files
history_dataframe = []
# finding current time and dat
current_time = time.localtime()
day = time.strftime("%d", current_time)
month = time.strftime("%B", current_time)
year = time.strftime("%Y", current_time)
date = f"{day}-{month}-{year}"

# check if user is signed in it can be check by if there is a file named with account.json already created
if not os.path.exists("files/account.json"):
    # calling function that takes user data and store in json file
    functions.sign_up()

# if account is already created directly start the chat
else:
    # retrieving user name and information to use in this software
    user_data_path = f"files/account.json"
    with open(f"{user_data_path}", "r") as json_file:
        user_data = json.load(json_file)
    full_name = user_data[0]["full_name"]

    # creating a json file of today's date to store history if is not already created
    history_file_path = f"files/history/{date}.json"
    if not os.path.exists(history_file_path):
        with open(history_file_path, 'w', encoding='utf-8') as json_file:
            # empty_data = {}
            # json.dump(empty_data, json_file)
            pass
    elif os.path.exists(history_file_path) and os.path.getsize(history_file_path) != 0:
        with open(history_file_path, 'r', encoding='utf-8') as json_file:
            file_content = json_file.read()
            if len(file_content) == 0:
                st.warning("No Content to Show here")
            else:
                try:
                    json_data = json.loads(file_content)
                    i = len(json_data)
                    history_dataframe = json_data
                except json.JSONDecodeError as e:
                    print(f"JSON decoding error: {e}")

    # applying centered styling to text
    st.markdown("""
    <style>
        .css-10trblm {
            text-align: center;
        }
    
    </style>
    """, unsafe_allow_html=True)
    # writing the date
    st.markdown(f"<p style='text-align: right;'>{date}</p>", unsafe_allow_html=True)
    st.title("Enhanced GPT Model")
# default text before chat
dot_style = "&#x25CF"
chat_default_text = f"{dot_style} Aslam u Alaikum!<br> {dot_style} I am Enhanced GPT<br> {dot_style} Write a " \
                    f"Text and get an Answer Record a Question and get an Answer<br> {dot_style} " \
                    f"I can read these Answers for you<br>"

typewriter_chat_default = functions.typewriter_text(chat_default_text)
st.markdown(typewriter_chat_default, unsafe_allow_html=True)
user_input = ""

files_path = f"../files/history"
json_history_files = glob.glob(f"{files_path}/*.json")
json_history_files = [file.replace("/", "\\") for file in json_history_files]
# st.text()


# if os.path.exists(history_file_path):
#     for i in range(len(history_dataframe)):
#         st.markdown(f"""{full_name}""", unsafe_allow_html=True)
#         st.info(history_dataframe[i]["user_input"])
#         st.markdown(f"Enhanced GPT", unsafe_allow_html=True)
#         st.write(history_dataframe[i]["chat_response"])
#         st.markdown(f"<p style='text-align: right;'>{history_dataframe[i][f'time']}</p>", unsafe_allow_html=True)

while True:
    # updating time
    formatted_time = time.strftime("%I:%M %p", current_time)

    # creating input box
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

    if 'user_input' not in st.session_state:
        st.session_state.user_input = {}
    user_input = st.text_area("", placeholder="Send a Message", key=f".stTextArea{i}")
    st.session_state.user_input[i] = user_input

    # if we get some input from the user
    if user_input != "":
        # st.markdown(f"""{full_name}""", unsafe_allow_html=True)
        # st.info(user_input)
        # st.markdown(f"<p style='text-align: right;'>{formatted_time}</p>", unsafe_allow_html=True)

        # creating instance of class chatbot
        chat = functions.Chatbot()
        # assigning a role
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]
        # getting response of user input
        chat_response = chat.get_response(user_input, messages)
        # typewriter_response = functions.typewriter_text(chat_response)
        # st.markdown("""Enhanced GPT""")
        # st.markdown(typewriter_response, unsafe_allow_html=True)
        # st.write(chat_response)

        # updating history dataframe
        history_dataframe.append({
            f"time": f"{formatted_time}",
            f"date": f"{day} : {month} : {year}",
            f"response_no": i,
            f"user_input": user_input,
            f"chat_response": chat_response
        })

        # st.session_state.time_list.append(formatted_time)

        st.session_state.current_page_responses.append({
            f"time": f"{formatted_time}",
            f"date": f"{day} : {month} : {year}",
            f"response_no": st.session_state.current_page_responses,
            f"user_input": user_input,
            f"chat_response": chat_response
        })
        st.session_state.time_list.append(history_dataframe[i][f'time'])
        j = 0
        for response in st.session_state.current_page_responses:
            st.write(full_name)
            user_i = response["user_input"]
            st.info(user_i)
            st.markdown("""Enhanced GPT""")
            st.write(response["chat_response"])
            st.markdown(f"<p style='text-align: right;'>{st.session_state.time_list[j]}</p>", unsafe_allow_html=True)
            j = j + 1

        functions.make_json_file(history_dataframe, history_file_path)
        i = i + 1
