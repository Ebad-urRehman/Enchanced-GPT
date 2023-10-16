import streamlit as st
import functions
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
    selection_image_type = ["🖌️ Create an Image", "✏️ Edit an Image", "🔄 Make Variations of Image"]
    selection = st.sidebar.selectbox("Selection Menu", selection_image_type)

    if selection == "🖌️ Create an Image":
        directory_name = f"files\\images\\Creation\\{date}"
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
            i = 0
        elif os.path.exists(directory_name):
            images = (glob.glob(f"{directory_name}/*.png"))
            i = len(images)
        st.markdown(f"<h1 style='text-align: center;'>🖌️ Create a New Image</h1>", unsafe_allow_html=True)
        st.info("""🖼 Create Stunning Images with Dall-E model\n
🖌️ Create an Image by scratch(Write a detailed prompt for better images)\n
✏️ Edit an Image(Change background and objects in image)\n
🔄 Make Variations of an Image(Dall-E can make variations of images for you)\n
    """)
        selection_image_size = ["256x256", "512x512", "1024x1024"]
        selection_size = st.sidebar.radio("Select Size", selection_image_size)

        # size selection menu
        if selection_size == "256x256":
            size = "256x256"
        elif selection_size == "512x512":
            size = "512x512"
        elif selection_size == "1024x1024":
            size = "1024x1024"
        no_of_images = st.sidebar.number_input("How many image Variations you want", min_value=1, max_value=10, value=1)

        user_input = functions.text_area_img()
        # making an instance of chatbot class
        image_bot = functions.Chatbot()
        if images:
            st.image(images)

        Generate_button = st.sidebar.button("🚀Generate Response✨")
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
                    st.success("✨ Image Generated Successfully✨")


    # when Edit image option selected
    elif selection == "✏️ Edit an Image":
        st.markdown(f"<h1 style='text-align: center;'>✏️ Edit an Image</h1>", unsafe_allow_html=True)
        # making two columns 1 for actual image other for masked image
        directory_name = f"files\\images\\Edited\\{date}"
        temp_file_actual = f"files\\temp_files\\actual-{date}.png"
        temp_file_masked = f"files\\temp_files\\masked-{date}.png"
        temp_dir = f"files\\temp_files"
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
                user_img_actual_formatted = functions.format_image(user_image_actual, 256)
                st.image(user_img_actual_formatted)
                functions.save_image_to_disk(user_img_actual_formatted, temp_file_actual)
                encoded_img_actual = functions.img_to_bytes(temp_file_actual)
            if user_image_masked:
                user_img_masked_formatted = functions.format_image(user_image_masked, 256)
                st.image(user_img_masked_formatted)
                functions.save_image_to_disk(user_img_masked_formatted, temp_file_masked)
                encoded_img_masked = functions.img_to_bytes(temp_file_masked)
        elif selection_size == "512x512":
            size = "512x512"
            if user_image_actual:
                user_img_actual_formatted = functions.format_image(user_image_actual, 512)
                st.image(user_img_actual_formatted)
                functions.save_image_to_disk(user_img_actual_formatted, temp_file_actual)
                encoded_img_actual = functions.img_to_bytes(temp_file_actual)
            if user_image_masked:
                user_img_masked_formatted = functions.format_image(user_image_masked, 512)
                st.image(user_img_masked_formatted)
                functions.save_image_to_disk(user_img_masked_formatted, temp_file_masked)
                encoded_img_masked = functions.img_to_bytes(temp_file_masked)
        elif selection_size == "1024x1024":
            size = "1024x1024"
            if user_image_actual:
                user_img_actual_formatted = functions.format_image(user_image_actual, 1024)
                st.image(user_img_actual_formatted)
                functions.save_image_to_disk(user_img_actual_formatted, temp_file_actual)
                encoded_img_actual = functions.img_to_bytes(temp_file_actual)
            if user_image_masked:
                user_img_masked_formatted = functions.format_image(user_image_masked, 1024)
                st.image(user_img_masked_formatted)
                functions.save_image_to_disk(user_img_masked_formatted, temp_file_masked)
                encoded_img_masked = functions.img_to_bytes(temp_file_masked)


        # taking inputs from user
        no_of_images = st.sidebar.number_input("How many image Variations you want", min_value=1, max_value=10, value=1)
        user_input = functions.text_area_img()
        # instance of image_bot
        image_bot = functions.Chatbot()
        Generate_button = st.sidebar.button("Generate Response")
        if Generate_button:
            if user_input == "":
                st.warning("Please Enter some Prompt")
            elif user_img_masked_formatted is None or user_img_actual_formatted is None:
                st.warning("Browse for Image files first")
            else:
                image_bot_response = image_bot.edit_image(temp_file_actual, temp_file_masked, user_input, size, no_of_images)
                for j, image_response_link in enumerate(image_bot_response):
                    img_name = f"{date}"

                    functions.save_image(directory_name, img_name, i, image_response_link)
                    i += 1
                st.success("✨ Image Generated Successfully✨")

    # deleting temporary file made for encoding
        if os.path.exists(temp_dir):
            functions.delete_all_images(temp_dir)

    # Make variation of images
    elif selection == "🔄 Make Variations of Image":
        st.markdown(f"<h1 style='text-align: center;'>🔄 Make Variations of an Image</h1>", unsafe_allow_html=True)

        # directories for storing history
        directory_name = f"files\\images\\Variations\\{date}"
        temp_file = f"files\\temp_files\\{date}.png"
        temp_dir = f"files\\temp_files"
        i = 0
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
            i = 0
        elif os.path.exists(directory_name):
            images = (glob.glob(f"{directory_name}/*.png"))
            i = len(images)

        user_image = st.file_uploader("Enter an Image file to get variations of it")
        user_img_formatted = None
        selection_image_size = ["256x256", "512x512", "1024x1024"]
        selection_size = st.sidebar.radio("Select Size", selection_image_size)
        # size selection menu
        if selection_size == "256x256":
            size = "256x256"
            if user_image:
                user_img_formatted = functions.format_image(user_image, 256)
                st.image(user_img_formatted)
                functions.save_image_to_disk(user_img_formatted, temp_file)
                encoded_img = functions.img_to_bytes(temp_file)
        elif selection_size == "512x512":
            size = "512x512"
            if user_image:
                user_img_formatted = functions.format_image(user_image, 512)
                st.image(user_img_formatted)
                functions.save_image_to_disk(user_img_formatted, temp_file)
                encoded_img = functions.img_to_bytes(temp_file)
        elif selection_size == "1024x1024":
            size = "1024x1024"
            if user_image:
                user_img_formatted = functions.format_image(user_image, 1024)
                st.image(user_img_formatted)
                functions.save_image_to_disk(user_img_formatted, temp_file)
                encoded_img = functions.img_to_bytes(temp_file)

        # taking inputs from user
        no_of_images = st.sidebar.number_input("How many image Variations you want", min_value=1, max_value=10,
                                               value=1)

        # instance of image_bot
        image_bot = functions.Chatbot()
        Generate_button = st.sidebar.button("🚀Generate Response✨")
        if Generate_button:
            if not user_img_formatted:
                st.warning("Browse for Image files first")
            else:
                image_bot_response = image_bot.make_variation_img(temp_file, size,
                                                          no_of_images)
                for j, image_response_link in enumerate(image_bot_response):
                    img_name = f"{date}"

                    functions.save_image(directory_name, img_name, i, image_response_link)
                    i += 1

                st.success("✨ Image Generated Successfully✨")

        # deleting temporary file made for encoding
        if os.path.exists(temp_dir):
            functions.delete_all_images(temp_dir)

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

    elif selection == "Image Editing History":
        # saving directory path
        directory_path = f"files\\images\\Edited"
        # finding all folders in directory
        history_dir = os.listdir(directory_path)
        history_dir_names = [dir for dir in history_dir]
        st.info(history_dir_names)
        # making a radio button based on directory names which means history days
        selected_day = st.sidebar.radio("Select Day", history_dir_names)
        # checking for every day which one is selected
        for history_dir_name in history_dir_names:
            if selected_day == history_dir_name:
                st.header("Edited Image History")
                # based on selected day diplaying images
                images = (glob.glob(f"{directory_path}\\{history_dir_name}/*.png"))
                if len(images) == 0:
                    st.warning("Nothing to show here")
                else:
                    st.image(images)

    elif selection == "Variations History":
        # saving directory path
        directory_path = f"files\\images\\Variations"
        # finding all folders in directory
        history_dir = os.listdir(directory_path)
        history_dir_names = [dir for dir in history_dir]
        # making a radio button based on directory names which means history days
        selected_day = st.sidebar.radio("Select Day", history_dir_names)
        # checking for every day which one is selected
        for history_dir_name in history_dir_names:
            if selected_day == history_dir_name:
                st.header("Image Variation History")
                st.info(f"Date : {history_dir_name}")
                # based on selected day diplaying images
                images = (glob.glob(f"{directory_path}\\{history_dir_name}/*.png"))
                if len(images) == 0:
                    st.warning("Nothing to show here")
                else:
                    st.image(images)

