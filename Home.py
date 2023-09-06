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

    api_key = os.getenv("OPEN AI API")
    dataframe = ["chat1", "chat2", "chat3"]



    st.markdown("""
    <style>
        .css-10trblm {
            text-align: center;
        }
        
        body {
            height: 100vh; /* Set the body height to 100% of the viewport height */
            margin: 0; /* Remove default body margin */
        }
        
        #sticky-container {
            position: relative;
            height: 100%; /* Set the height of the container to 100% of the viewport height */
        }
        
        .input {
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
            
                }
    </style>
    
    
    
    
     <textarea class="input" type="text" placeholder="Send a Message">
    """, unsafe_allow_html=True)


st.markdown("""
<style>
  /* Define the typing animation */
  @keyframes typing {
    from { width: 0; }
    to { width: 100%; }
  }

  /* Define a blinking cursor animation */
  @keyframes blink {
    50% { border-color: transparent; }
  }

  /* Apply the animation to the text */
  .typewriter-text {
    white-space: nowrap; /* Prevent text from wrapping */
    overflow: hidden;   /* Hide overflow */
    border-right: 2px solid #000; /* Add a cursor effect */
    animation: typing 3s steps(40), blink 1s step-end infinite; /* Adjust duration and steps */
  }
</style>""", unsafe_allow_html=True)
st.markdown('<p class = "typewriter-text">I am Enhanced GPT', unsafe_allow_html=True)

    # user_input = st.text_area("Enter Text Message here", max_chars=4000, placeholder="Send a Message")

    # # creating instance of class Chatbot
    # chat = functions.Chatbot()
    #
    # chat_response = chat.get_response(user_input)
    #
    # st.text(chat_response)