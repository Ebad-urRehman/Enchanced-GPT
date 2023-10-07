import os
import openai
import streamlit as st
import json
import requests


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

    def get_response(self, user_input, messages, no_of_tokens, temp):
        messages.append({"role": "user", "content": user_input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            # prompt = user_input,
            max_tokens=no_of_tokens,
            temperature=temp
        )
        response = chat.choices[0].message.content
        # response = ""
        # if user_input == "asdf":
        #     response = "I am fine!\n How are you I am output I am output I am output I am output I am output I am output I am output I am output I am output I am output I am output I am outputv I am output"
        return  response
    def get_image(self, user_input, size, no_of_images):
            response = openai.Image.create(
                prompt=user_input,
                n=no_of_images,
                size=size
            )
            # image_url = response['data'][0]['url']
            image_urls = [result['url'] for result in response['data']]
            # image_urls = {"0":"https://oaidalleapiprodscus.blob.core.windows.net/private/org-7yMSDDPots0mp25LaesEBh5p/user-eJVeNouBg5vAW280BHorayK8/img-KulIRbr2KRdKWK0UUyo2Uc2q.png?st=2023-09-27T15%3A34%3A31Z&se=2023-09-27T17%3A34%3A31Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-09-26T23%3A43%3A09Z&ske=2023-09-27T23%3A43%3A09Z&sks=b&skv=2021-08-06&sig=wikUgj1ZXq9xROJo2uG8knQoi8ycuFE07P4y53zVL3E%3D"}
            # image_urls = [
            #     "https://img.freepik.com/free-photo/luxurious-car-parked-highway-with-illuminated-headlight-sunset_181624-60607.jpg",
            #     "https://img.freepik.com/premium-photo/bangkok-thailand-08082022-lamborghini-luxury-super-car-fast-sports-premium-lighting-background-3d-illustration_67092-1599.jpg"]
            # if user_input == "asdf":
            #     st.write(image_urls)
            return image_urls

    def edit_image(self, org_image, masked_img, user_input, size, no_of_images):
        response = openai.Image.create_edit(
            image=open(org_image),
            mask=open(masked_img),
            prompt=user_input,
            n=no_of_images,
            size=size
        )
        image_urls = [result['url'] for result in response['data']]
        st.write(image_urls)
        return image_urls


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


def text_area_img():
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

    user_input = st.text_area("", placeholder="Enter more details for better image")
    return user_input


def download_image(url, save_path):
    try:
        # Send an HTTP request to the URL to get the image data
        response = requests.get(url)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Save the image data to a file in binary mode
            with open(save_path, 'wb') as file:
                file.write(response.content)
            with open(save_path, 'rb') as file:
                myfile = file.read()
            st.image(myfile)
            st.info("Image downloaded successfully.")
            return myfile
        else:
            st.warning("Failed to download image because of network issue")
    except Exception as e:
        st.info("Error:" + str(e))


if __name__ == "__main__":
    pass
