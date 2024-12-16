import os
from openai import OpenAI
import streamlit as st
import json
import requests
from io import BytesIO
from PIL import Image
from pathlib import Path
import base64
# from gtts import gTTS
# from googletrans import Translator
from pydub import AudioSegment
from pydub.playback import play


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
        dob = f"{day}/{mounth}/{year}"
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
        self.client = OpenAI(api_key=os.getenv("OPENAI_KEY"))
    def get_response(self, user_input, messages, no_of_tokens, temp, selected_model):
        messages.append({"role": "user", "content": user_input})
        chat = self.client.chat.completions.create(
            model=selected_model,
            messages=messages,
            max_tokens=no_of_tokens,
            temperature=temp
        )
        response = chat.choices[0].message.content
        return response


    def get_o1_response(self, user_input, messages, max_tokens, selected_model):
        messages.append({"role": "user", "content": user_input})
        chat = self.client.chat.completions.create(
            model=selected_model,
            messages=messages,
            max_completion_tokens=max_tokens,
        )
        response = chat.choices[0].message.content
        return response

    def get_image(self, user_input, size, no_of_images):
        response = self.client.Image.create(
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

    def edit_image(self, org_image_path, masked_img_path, user_input, size, no_of_images):
        with open(org_image_path, 'rb') as org_image_file, open(masked_img_path, 'rb') as masked_img_file:
            response = self.client.Image.create_edit(
                image=org_image_file,
                mask=masked_img_file,
                prompt=user_input,
                n=no_of_images,
                size=size
            )
        image_urls = [result['url'] for result in response['data']]
        st.write(image_urls)
        return image_urls

    def make_variation_img(self, image_path, size, no_of_images):
        with open(image_path, 'rb') as image_file:
            response = self.client.Image.create_variation(
                image=image_file,
                n=no_of_images,
                size=size
            )
        image_urls = [result['url'] for result in response['data']]
        st.write(image_urls)
        return image_urls

# class TextToSpeech():
#     def __init__(self):
#         self.translator = Translator()

#     def get_lang_dict(self):
#         dict = {"Auto Detect": "auto",
#         "عربی Arabic":"ar",
#         "Bengali بنگالی": "bn",
#         "English": "en",
#         "اردو Urdu": "ur",
#         "Hindi ہندی": "hi"
#         }
#         return dict
#     def text_to_speech(self, text, output_lang, mode):
#         if output_lang == "auto":
#             output_lang = self.translator.detect(text).lang
#         tts = gTTS(text, lang=output_lang, slow=mode)
#         file_path = "files/temp_files/temp.mp3"
#         tts.save(file_path)
#         st.audio(file_path)

#     def trans(self, text, input_lang, output_lang):
#         if input_lang == "auto":
#             input_lang = self.translator.detect(text).lang
#         if output_lang == "auto":
#             output_lang = "en"
#         translation = self.translator.translate(text=text, src=input_lang, dest=output_lang)
#         translated_text = translation.text
#         return translated_text

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

def format_image(user_image, size):
    image_stream_actual = BytesIO(user_image.read())
    user_img_formatted = Image.open(image_stream_actual)
    user_img_formatted = user_img_formatted.resize((size, size))
    return user_img_formatted

def save_image_to_disk(image, savepath):
    image.save(savepath)

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded_img = base64.b64encode(img_bytes).decode()
    return encoded_img


def save_image(directory_name, img_name, i, image_response_link):
    st.info("Saving Image to disk")
    save_path = f"{directory_name}/{img_name}-{i}.png"
    download_image(image_response_link, save_path)

def delete_all_images(dir):
    check = os.listdir(dir)
    if check:
        for filename in os.listdir(dir):
            file_path = os.path.join(dir, filename)
            os.remove(file_path)



def png_to_ascii(image_path):
    image = Image.open(image_path)
    width, height = image.size

    aspect_ratio = height/width
    new_width = 100
    new_height = int(aspect_ratio * new_width * 0.55)

    resized_image = image.resize((new_width, new_height))
    grayscale_image = resized_image.convert("L")

    pixels = grayscale_image.getdata()
    ascii_chars = "@%#*+=-:. "

    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ascii_chars[pixel_value // 25]

    ascii_str_len = len(ascii_str)
    ascii_img = [ascii_str[index: index + new_width] for index in range(0, ascii_str_len, new_width)]
    return "\n".join(ascii_img)


if __name__ == "__main__":
    pass
