import os
import openai
import streamlit as st

def sign_up():
    # form = st.form("Sign in Form")
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
                    return [f_name, l_name, email_ad, dob]

                else:
                    st.warning("Enter a valid Email Address")
            else:
                st.warning("Please fill all required fields")
        return [0, 0, 0, 0]




class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv("OPEN AI API")


    def get_response(self, user_input):
        # response = openai.ChatCompletion.create(
        #     model="text-davinci-003",
        #     prompt = user_input,
        #     max_tokens = 3000,
        #     temprature = 0.5
        # ).choices[0].text
        response = ""
        if user_input == "How are you":
            response = "I am fine!\n How are you"
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Hi How are you")
    print(response)