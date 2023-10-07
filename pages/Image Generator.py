import streamlit as st
import functions
from io import BytesIO
from PIL import Image
import time
import os
import glob


# finding current time and dat
current_time = time.localtime()
day = time.strftime("%d", current_time)
month = time.strftime("%B", current_time)
year = time.strftime("%Y", current_time)
date = f"{day}-{month}-{year}"

# model options to be showed on sidebar
options = ["Generate new images", "History"]

selected_option = st.sidebar.radio("", options)
i = 0
if selected_option == "Generate new images":
    selection_image_type = ["Create an Image", "Edit an Image", "Make variations of Image"]
    selection = st.sidebar.selectbox("Selection Menu", selection_image_type)

    if selection == "Create an Image":
        directory_name = f"files\\images\\Creation\\{date}"
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
            i = 0
        elif os.path.exists(directory_name):
            images = (glob.glob(f"{directory_name}/*.png"))
            i = len(images)
        st.markdown(f"<h1 style='text-align: center;'>Create a New Image</h1>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            selection_image_size = ["256x256", "512x512", "1024x1024"]
            selection_size = st.sidebar.radio("Select Size", selection_image_size)

            # size selection menu
            if selection_size == "256x256":
                size = "256x256"
            elif selection_size == "512x512":
                size = "512x512"
            elif selection_size == "1024x1024":
                size = "1024x1024"
            no_of_images = st.sidebar.number_input("How many image variations you want", min_value=1, max_value=10, value=1)

        user_input = functions.text_area_img()
        # making an instance of chatbot class
        image_bot = functions.Chatbot()

        st.image(images)

        Generate_button = st.sidebar.button("Generate Response")
        if Generate_button:
            if user_input == "":
                st.warning("Please Enter some Prompt")
            else:
                image_bot_response = image_bot.get_image(user_input, size, no_of_images)
                for j, image_response_link in enumerate(image_bot_response):

                    img_name = f"{date}"
                    def save_image():
                        st.info("Saving Image to disk")
                        save_path = f"{directory_name}\\{img_name}-{i}.png"
                        functions.download_image(image_response_link, save_path)

                    save_image()
                    i += 1


    # when Edit image option selected
    elif selection == "Edit an Image":
        st.header("Edit an Image")
        # making two columns 1 for actual image other for masked image
        directory_name = f"files\\images\\Edited\\{date}"
        i = 0
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
            i = 0
        elif os.path.exists(directory_name):
            images = (glob.glob(f"{directory_name}/*.png"))
            i = len(images)
        col1, col2 = st.columns(2)
        with col1:
            st.info("Enter actual image here")
            user_image_actual = st.file_uploader("", key="file_up1")
            # resizing the Image
            width, height = 256, 256
            # image = user_image.resize((width, height))
            if user_image_actual:
                st.image(user_image_actual)

        with col2:
            st.info("Enter masked image here")
            user_image_masked = st.file_uploader("", key="file_up2")
            # resizing the Image
            width2, height2 = 256, 256
            # image = user_image.resize((width, height))
            if user_image_masked:
                st.image(user_image_masked)
        user_img_actual_formatted = None
        user_img_masked_formatted = None
        selection_image_size = ["256x256", "512x512", "1024x1024"]
        selection_size = st.sidebar.radio("Select Size", selection_image_size)
        # size selection menu
        if selection_size == "256x256":
            size = "256x256"
            if user_image_actual:
                image_stream_actual = BytesIO(user_image_actual.read())
                user_img_actual_formatted = Image.open(image_stream_actual)
                user_img_actual_formatted = user_img_actual_formatted.resize((256, 256))
                user_img_actual_formatted = user_img_actual_formatted.convert("RGB")
                st.image(user_img_actual_formatted)
                with BytesIO() as buffer:
                    user_img_actual_formatted.save(buffer, format="JPEG")
                    actual_img_bytes = buffer.getvalue()
            if user_image_masked:
                image_stream_mask = BytesIO(user_image_masked.read())
                user_img_masked_formatted = Image.open(image_stream_mask)
                user_img_masked_formatted = user_img_masked_formatted.resize((256, 256))
                user_img_masked_formatted = user_img_masked_formatted.convert("RGB")
                st.image(user_img_masked_formatted)
                with BytesIO() as buffer:
                    user_img_masked_formatted.save(buffer, format="JPEG")
                    masked_img_bytes = buffer.getvalue()
        elif selection_size == "512x512":
            size = "512x512"
            if user_image_actual:
                image_stream_actual = BytesIO(user_image_actual.read())
                user_img_actual_formatted = Image.open(image_stream_actual)
                user_img_actual_formatted = user_img_actual_formatted.resize((512, 512))
                user_img_actual_formatted = user_img_actual_formatted.convert("RGB")
                st.image(user_img_actual_formatted)
                with BytesIO() as buffer:
                    user_img_actual_formatted.save(buffer, format="JPEG")
                    actual_img_bytes = buffer.getvalue()
            if user_image_masked:
                image_stream_mask = BytesIO(user_image_masked.read())
                user_img_masked_formatted = Image.open(image_stream_mask)
                user_img_masked_formatted = user_img_masked_formatted.resize((512, 512))
                user_img_masked_formatted = user_img_masked_formatted.convert("RGB")
                st.image(user_img_masked_formatted)
                with BytesIO() as buffer:
                    user_img_masked_formatted.save(buffer, format="JPEG")
                    masked_img_bytes = buffer.getvalue()
        elif selection_size == "1024x1024":
            size = "1024x1024"
            if user_image_actual:
                image_stream_actual = BytesIO(user_image_actual.read())
                user_img_actual_formatted = Image.open(image_stream_actual)
                user_img_actual_formatted = user_img_actual_formatted.resize((1024, 1024))
                user_img_actual_formatted = user_img_actual_formatted.convert("RGB")
                st.image(user_img_actual_formatted)
                with BytesIO() as buffer:
                    user_img_actual_formatted.save(buffer, format="JPEG")
                    actual_img_bytes = buffer.getvalue()
            if user_image_masked:
                image_stream_masked = BytesIO(user_image_actual.read())
                user_img_masked_formatted = Image.open(image_stream_masked)
                user_img_masked_formatted = user_img_masked_formatted.resize((1024, 1024))
                user_img_masked_formatted = user_img_masked_formatted.convert("RGB")
                st.image(user_img_masked_formatted)
                # with open(user_img_masked_formatted, "rb") as img:
                with BytesIO() as buffer:
                    user_img_masked_formatted.save(buffer, format="JPEG")
                    masked_img_bytes = buffer.getvalue()
        no_of_images = st.sidebar.number_input("How many image variations you want", min_value=1, max_value=10, value=1)
        user_input = functions.text_area_img()
        image_bot = functions.Chatbot()
        Generate_button = st.sidebar.button("Generate Response")
        if Generate_button:
            if user_input == "":
                st.warning("Please Enter some Prompt")
            elif user_img_masked_formatted is None or user_img_actual_formatted is None:
                st.warning("Browse for Image files first")
            else:
                # with open(user_img_masked_formatted, "rb") as img_act:
                #     actual_img_bytes = img_act.read
                image_bot_response = image_bot.edit_image(actual_img_bytes, masked_img_bytes, user_input, size, no_of_images)
                for j, image_response_link in enumerate(image_bot_response):
                    img_name = f"{date}"

                    def save_image():
                        st.info("Saving Image to disk")
                        save_path = f"{directory_name}\\{img_name}-{i}.png"
                        functions.download_image(image_response_link, save_path)

                    save_image()
                    i += 1
                # image_bot_response = image_bot.get_image(user_input, size, no_of_images=1)
                # for image in image_bot_response:
                #     st.image(image_bot_response)
                #     st.write(image_bot_response)
                st.success("Generating Response")

    # Make variation of images
    elif selection == selection_image_type[2]:
        st.header("Make Varaitions of Images")
        user_image = st.file_uploader("Enter a Valid image file ")
        if user_image:
            # resizing the Image
            width, height = 256, 256
            image = user_image.resize((width, height))
            st.image(user_image)
        selection_image_size = ["256x256", "512x512", "1024x1024"]
        selection_size = st.radio("Select Size", selection_image_size)
        # setting size
        if selection_size == selection_image_size[0]:
            size = "256x256"
        elif selection_size == selection_image_size[1]:
            size = "512x512"
        elif selection_size == selection_image_size[2]:
            size = "1024x1024"




if selected_option == "History":
    selection_image_type = ["Image Creation History", "Image Editing History", "Variations History"]
    selection = st.sidebar.selectbox("Selection Menu", selection_image_type)
    if selection == "Image Creation History":
        # saving directory path
        directory_path = f"files\\images\\Creation"
        # finding all folders in directory
        history_dir = os.listdir(directory_path)
        history_dir_names = [dir for dir in history_dir]
        # making a radio button based on directory names which means history days
        selected_day = st.sidebar.radio("Select Day", history_dir_names)
        # checking for every day which one is selected
        for history_dir_name in history_dir_names:
            if selected_day == history_dir_name:
                st.header("Image Creation History")
                st.info(f"Date : {history_dir_name}")
                # based on selected day diplaying images
                images = (glob.glob(f"{directory_path}\\{history_dir_name}/*.png"))
                if len(images) == 0:
                    st.warning("Nothing to show here")
                else:
                    st.image(images)

        if selection == "Image Editing History":
            # saving directory path
            directory_path = f"files\\images\\Creation"
            # finding all folders in directory
            history_dir = os.listdir(directory_path)
            history_dir_names = [dir for dir in history_dir]
            # making a radio button based on directory names which means history days
            selected_day = st.sidebar.radio("Select Day", history_dir_names)
            # checking for every day which one is selected
            for history_dir_name in history_dir_names:
                if selected_day == history_dir_name:
                    st.header("Image Creation History")
                    st.info(f"Date : {history_dir_name}")
                    # based on selected day diplaying images
                    images = (glob.glob(f"{directory_path}\\{history_dir_name}/*.png"))
                    if len(images) == 0:
                        st.warning("Nothing to show here")
                    else:
                        st.image(images)

