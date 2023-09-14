import streamlit as st
import glob
import json


files_path = f"files/history"

files = (glob.glob(f"{files_path}/*.json"))
radio_buttons = []
for file in files:
    formatted_path = file.replace("\\", "/")
    formatted_name = file[14:-5]
    radio_buttons.append(formatted_name)
print(radio_buttons)
selection = st.sidebar.radio("Chat HISTORY", radio_buttons)
print(files)

total_files = len(files)
try:
    for i in range(total_files):
        if selection == radio_buttons[i]:
            with open(rf"C:\Users\infall\PycharmProjects\Enhanced chatbot\files\history\{radio_buttons[i]}.json", "r") as file:
                json_data = json.load(file)
            total_responses = len(json_data)
            st.header(f"{json_data[0][f'date']}")
            for i in range(total_responses):
                st.info(f"{json_data[i]['user_input']}")
                st.markdown(f"<p style='text-align: right;'>{json_data[i]['time']}</p>", unsafe_allow_html=True)
                st.write(f"{json_data[i]['chat_response']}")
                st.markdown(f"<p style='text-align: right;'>{json_data[i]['time']}</p>", unsafe_allow_html=True)
except json.JSONDecodeError as e:
    st.warning("No Chat on this date")
