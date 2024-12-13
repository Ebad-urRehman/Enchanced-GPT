import streamlit as st
import glob
import json

st.markdown(f"<h1 style='text-align: center;'>✨Enhanced GPT Model✨</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: left;'>History🧾🔁</h2>", unsafe_allow_html=True)
files_path = f"files/history"
# extracting all files from directory filepath
files = (glob.glob(f"{files_path}/*.json"))
radio_buttons = []
# formatting the names of file in readable way DD-MM-YY
for file in files:
    formatted_path = file.replace("\\", "/")
    formatted_name = file[14:-5]
    radio_buttons.append(formatted_name)

selection = st.sidebar.radio("Chat HISTORY", radio_buttons)

total_files = len(files)
# loading selected file form history files and displaying data
try:
    for i in range(total_files):
        if selection == radio_buttons[i]:
            with open(rf"files/history/{radio_buttons[i]}.json", "r") as file:
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
