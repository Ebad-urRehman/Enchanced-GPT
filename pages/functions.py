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
from utils.account_settings import get_api_key



class Chatbot:
    def __init__(self):
        self.api_key = get_api_key()
        self.client = OpenAI(api_key=self.api_key)
    def get_response(self, user_input, messages, no_of_tokens, temp, selected_model):
        try:
            messages.append({"role": "user", "content": user_input})
            chat = self.client.chat.completions.create(
                model=selected_model,
                messages=messages,
                max_tokens=no_of_tokens,
                temperature=temp
            )
            response = chat.choices[0].message.content
            return response
        except Exception as e:
            st.warning(e)


    def get_o1_response(self, user_input, messages, max_tokens, selected_model):
        try:
            messages.append({"role": "user", "content": user_input})
            chat = self.client.chat.completions.create(
                model=selected_model,
                messages=messages,
                max_completion_tokens=max_tokens,
            )
            response = chat.choices[0].message.content
            return response
        except Exception as e:
            st.warning(e)
    


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
