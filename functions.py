import os
import openai
import streamlit as st
import json


# function for sign up if signed up
def sign_up():
    with st.form("Sign in Form"):
        st.header("Sign up")
        col1, col2 = st.columns(2)
        f_name = col1.text_input("First Name", placeholder="First Name")
        l_name = col2.text_input("Last Name", placeholder="Last Name")
        email_ad = st.text_input("Email Address", placeholder="Email Address")
        day, mounth, year = st.columns(3)
        day = day.text_input("Enter Day", placeholder="Enter Day")
        mounth = mounth.text_input("Enter Mounth", placeholder="Enter Mounth")
        year = year.text_input("Enter Year", placeholder="Enter Year")
        dob = f"{day}\{mounth}\{year}"
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            if f_name != "" and l_name != "" and email_ad != "" and day != "" and mounth != "" and year != "":
                if email_ad.endswith("@gmail.com"):
                    if not os.path.exists("files/account.txt"):
                        with open("files/account.txt", "w") as account_file:
                            account_file.write(f"First Name : {f_name}\n"
                                               f"Last Name : {l_name}\n"
                                               f"Email : {email_ad}\n"
                                               f"day\mounth\year : {dob}"
                                               )
                            full_name = f"{f_name}{l_name}"
                    # storing data as a dictionary
                    user_data = [{
                        "full_name": f"{f_name}{l_name}",
                        "f_name": f"{f_name}",
                        "l_name": f"{l_name}",
                        "email_ad": f"{email_ad}",
                        "dob": f"{dob}"
                    }]
                    user_data_path = f"files/account.json"
                    # storing data in json file
                    with open(user_data_path, 'w') as json_file:
                        json.dump(user_data, json_file, indent=4)

                    print(user_data)
                    return [f_name, l_name, email_ad, dob]

                else:
                    st.warning("Enter a valid Email Address")
            else:
                st.warning("Please fill all required fields")
        return


class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv("OPEN AI KEY")

    def get_response(self, user_input, messages):
        messages.append({"role": "user", "content": user_input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            # prompt = user_input,
            max_tokens=1000,
            temperature=0.5
        )
        response = chat.choices[0].message.content
        # response = ""
        # if user_input == "asdf":
        #     response = "I am fine!\n How are you I am output I am output I am output I am output I am output I am output I am output I am output I am output I am output I am output I am outputv I am output"
        return response


def typewriter_text(text):
    typewriter_style = f"""
    <style>
        /* Define the typing animation */
        @keyframes typing {{
            from {{ width: 0; }}
            to {{ width: 100%; }}
        }}

        /* Define a blinking cursor animation */
        @keyframes blink {{
            50% {{ border-color: transparent; }}
        }}

        /* Apply the animation to the text */
        .typewriter {{
            /*white-space: nowrap; Prevent text from wrapping */
            /*overflow: hidden;   /* Hide overflow */
            border-right: 2px solid #000; /* Add a cursor effect */
            animation: typing 3s steps(40), blink 1s step-end 1s; /* Adjust duration and steps */
            color: rgb(199, 235, 255);
            background-color: rgb(0, 51, 102);
            border-radius: 13px;
            -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
            -webkit-box-pack: justify;
            justify-content: space-between;
        }}
    </style>
    """
    # combining typewriter text effect with our program text
    typewriter_text = f'<p class="typewriter">{text}</p>'
    return typewriter_style + typewriter_text


def make_json_file(dataframe, filename):
    with open(filename, 'w') as json_file:
        json.dump(dataframe, json_file, indent=4)


if __name__ == "__main__":
    pass
