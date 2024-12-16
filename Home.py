import os
import streamlit as st
import pages.functions as functions
import time
import json
import glob
import utils.home_utils as home_utils
from utils.account_settings import validate_account_info, store_account_info, get_user_name

# i is denoting no of total number of responses here in a day
i = 0

# current_page_responses stores data of responses in an acive chat
# used to preserve previous responses during a chat
if 'current_page_responses' not in st.session_state:
    st.session_state.current_page_responses = []
# time variable to show unique time for each response while in a chat
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

# inputting a role from user
roles = ["🎞 Default Role", "📲 Custom Role"]
models = ["🚀GPT-3.5-Turbo", "🤖GPT-4", "🪶o1-Mini", "🛠️o1-Preview"]
temperature = st.sidebar.slider("Temprature 🌡", 0.0, 1.0, 0.5, 0.01)
number_of_tokens = st.sidebar.slider("Number of Tokens 🔢", 1000, 4096, 1000, 200)
role_selection = st.sidebar.selectbox("Enter the role here", roles)
model_selection = st.sidebar.radio("Select model : ", models)

if role_selection == "🎞 Default Role":
    role ="You are a helpful assistant."
elif role_selection == "📲 Custom Role":
    role = st.sidebar.text_input("Assign a Role")

if model_selection == "🚀GPT-3.5-Turbo":
    model = "gpt-3.5-turbo"
elif model_selection == 'GPT-4':
    model = "gpt-4"
elif model_selection == "🪶o1-Mini":
    model = "o1-mini"
elif model_selection == "🛠️o1-Preview":
    model = "o1-preview"


if not validate_account_info():
    store_account_info()

else:
    full_name = get_user_name()

    # creating a json file of today's date to store history if is not already created
    history_file_path = f"files/history/{date}.json"
    if not os.path.exists(history_file_path):
        with open(history_file_path, 'w', encoding='utf-8') as json_file:
            pass
    elif os.path.exists(history_file_path) and os.path.getsize(history_file_path) != 0:
        with open(history_file_path, 'r', encoding='utf-8') as json_file:
            file_content = json_file.read()
            if len(file_content) == 0:
                st.warning("No Content to Show here")
            else:
                try:
                    json_data = json.loads(file_content)
                    # if there are previous reponses in a chat it updates the number to them
                    i = len(json_data)
                    history_dataframe = json_data
                except json.JSONDecodeError as e:
                    print(f"JSON decoding error: {e}")

    # writing the date
    st.markdown(home_utils.date_formatted(date), unsafe_allow_html=True)
    st.markdown(home_utils.heading_formatted('✨Enhanced GPT Model✨'), unsafe_allow_html=True)

st.info(home_utils.chat_default_text())
user_input = ""


# extracting file paths for each json history data file
files_path = f"../files/history"
json_history_files = glob.glob(f"{files_path}/*.json")
json_history_files = [file.replace("/", "\\") for file in json_history_files]
# st.text()

# while True:
# updating time
formatted_time = time.strftime("%I:%M %p", current_time)

# creating input box styling
st.markdown(home_utils.styles['textAreaStyle'], unsafe_allow_html=True)
# creating input box
if 'user_input' not in st.session_state:
    st.session_state.user_input = {}

user_input = st.text_area("", placeholder="Send a Message", key=f".stTextArea{i}")

uploaded_file = st.file_uploader("Choose a file", key="hidden_file_input", label_visibility="collapsed")

st.session_state.user_input[i] = user_input
 
col1, col2 = st.columns(2)

if user_input == "":
    with col1:
        st.info(home_utils.user_guide1())
    with col2:
        # st.image("ai.png")
        st.info(home_utils.user_guide2())
        

# if we get some input from the user
if user_input != "":
    # creating instance of class chatbot
    chat = functions.Chatbot()

    if uploaded_file:
        file_data = uploaded_file.getvalue()
        user_input = f'Here is content from a file {file_data} I want to ask : {user_input}'

    # assigning a role
    if model == 'gpt-3.5-turbo' or model=='gpt-4':
        messages = [
            {"role": "system", "content": f"{role} + maybe sometimes you are provided with some text from files, read that content and answer about that files"},
        ]
        # getting response of user input
        chat_response = chat.get_response(user_input, messages, number_of_tokens, temperature, model)   
    else:
        messages = []
        chat_response = chat.get_o1_response(user_input, messages, number_of_tokens, model)

    

    

    # updating history dataframe
    history_dataframe.append({
        f"time": f"{formatted_time}",
        f"date": f"{day} : {month} : {year}",
        f"response_no": i,
        f"user_input": user_input,
        f"chat_response": chat_response
    })

    st.session_state.current_page_responses.append({
        f"time": f"{formatted_time}",
        f"date": f"{day} : {month} : {year}",
        f"response_no": st.session_state.current_page_responses,
        f"user_input": user_input,
        f"chat_response": chat_response
    })
    st.session_state.time_list.append(history_dataframe[i][f'time'])
    # j for keep track of old responses in active chat
    # it is done because active chat lose its old responses when a new one is entered
    j = 0
    for response in st.session_state.current_page_responses:
        st.write(full_name)
        user_i = response["user_input"]
        st.info(user_i)
        st.markdown("""Enhanced GPT""")
        st.write(response["chat_response"])
        st.markdown(f"<p style='text-align: right;'>{st.session_state.time_list[j]}</p>", unsafe_allow_html=True)
        j = j + 1
    # creating json history file and storing data in it
    functions.make_json_file(history_dataframe, history_file_path)
    i = i + 1
