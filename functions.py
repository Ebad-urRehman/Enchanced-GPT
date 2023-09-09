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
        openai.api_key = os.getenv("OPEN AI KEY")


    def get_response(self, user_input):
        # messages = [
        #     {"role": "system", "content": "You are a helpful assistant."},
        # ]
        # messages.append({"role": "user", "content": user_input})
        # chat = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=messages,
        #     # prompt = user_input,
        #     max_tokens=1000,
        #     temperature=0.5
        # )
        # response = chat.choices[0].message.content
        response = ""
        if user_input == "asdf":
            response = "I am fine!\n How are you I am output I am output I am output I am output I am output I am output I am output I am output I am output I am output I am output I am outputv I am output"
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
            background-color: rgb(23, 45, 67);
            border-radius: 13px;
            -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        }}
    </style>
    """

    typewriter_text = f'<p class="typewriter">{text}</p>'
    return typewriter_style + typewriter_text


def input_at_bottom():
    at_bottom_style = f"""
    <html>
    <form>
    <div>
        <label for="user-input">User Input</label><br>
        <input type="text" name = "UserInput"
    </div> 
    </div>
        <button type= "submit">Submit<button>
    </form>
    </html>

    form.addEventListener('submit', (e) => 
    {{
        e.preventDefault();
        const fd = new FormData(form);
        console.log(fd)   
    }}
    <style>
        .input {{
            min-height: 50px;
            width: 58%;
            position: fixed;
            bottom: 0;
            background-color: #333;
            padding: 10px;
            z-index: 999;
            border:0px solid white;
            border-radius:13px;
            text-color: #F5F5F5
            caret-color: rgb(250, 250, 250);
            color: rgb(250, 250, 250);
            padding-bottom: 10px;
            outline: none;
                        
            }}
        .st-aj{{
        position: fixed;
        bottom: 0;
        }}
    
    </style>
    """
    # input_style = f'<textarea class ="input" type="text" placeholder="Send a Message" >'
    input_style = f'{at_bottom_style}\n<textarea class="input" type="text" placeholder="Send a Message"></textarea>'
    return input_style

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Hi How are you")
    print(response)