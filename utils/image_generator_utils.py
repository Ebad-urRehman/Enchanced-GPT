import base64
import os
from io import BytesIO
from pathlib import Path
from PIL import Image
import requests
import streamlit as st
from openai import OpenAI
from utils.account_settings import get_api_key

class Chatbot():
    def __init__(self):
        self.api_key = get_api_key()
        self.client = OpenAI(
            api_key=self.api_key
        )


    def get_image(self, user_input, size, model, quality):
        response = self.client.images.generate(
            model=model,
            prompt=user_input,
            size=size,
            quality=quality,
            n=1,
        )
        image_url = response.data[0].url
        return image_url
    
    def get_image_dall_e2(self, user_input, size, style):
        response = self.client.images.generate(
            model='dall-e-2',
            prompt=user_input,
            size=size,
            style=style,
            n=1,
        )
        image_url = response.data[0].url
        return image_url


    def edit_image(self, org_image_path, masked_img_path, user_input, size, no_of_images):
        with open(org_image_path, 'rb') as org_image_file, open(masked_img_path, 'rb') as masked_img_file:
            response = self.client.images.edit(
                model="dall-e-2",
                image=org_image_file,
                mask=masked_img_file,
                prompt=user_input,
                n=no_of_images,
                size=size
            )
        image_urls = [response.data[0].url for i in range(no_of_images)]
        st.write(image_urls)
        return image_urls

    def make_variation_img(self, image_path, size, no_of_images):
        response = self.client.images.create_variation(
            image=open(image_path, "rb"),
            n=no_of_images,
            size=size
        )
        image_urls = [response.data[0].url for i in range(no_of_images)]
        st.write(image_urls)
        return image_urls


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