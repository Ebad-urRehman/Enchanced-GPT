import streamlit as st
import openai
import pandas
import time
from pathlib import Path
import os
from utils.account_settings import get_api_key

# ------------------------------------------FUNCTIONS CODE-------------------------------------


# making a class chatbot
class Chatbot:
    def get_seo_optimized_words(self, messages):
        try:
            my_api_key = get_api_key()
            client = openai.OpenAI(api_key=my_api_key)
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                max_tokens=300,
            )
            return response.choices[0].message.content

        except Exception as e:
            return False


# get user download path
def get_download_path():
    # Get the user's home directory
    home_dir = Path.home()

    # find the desktop directory based on the operating system
    download_dir = home_dir / 'Downloads',
    return download_dir

# save csv file in download path
def end_program():
    st.success(f"File Downloaded successfully.")
    st.dataframe(st.session_state.mydataframe)
    st.stop()


# -----------------------------Main File Code----------------------------

# finding current date and time
current_time = time.localtime()
day = time.strftime("%d", current_time)
month = time.strftime("%B", current_time)
year = time.strftime("%Y", current_time)
date = f"{day}-{month}-{year}"
formatted_time = time.strftime("%I-%M-%S %p", current_time)

# variables declaration
links_input = ""
url_list = []
valid_url_list = []
invalid_url_list = []
response_list = []
valid_response_list = []
invalid_response_list = []
output_csv = None
# i is used to confirm that invalid url are present or not for one time
i = 1
# j is used to calculate invalid number of urls
j = 0
response = None 

# download button state
button_clicked = False

csv_file_name = date


st.markdown(f"<p style='text-align: right;'>{date}</p>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center;'>🖼️Image to SEO keywords⚙️🔧</h1>", unsafe_allow_html=True)
st.info("""🌐Input Urls of Images\n
📄Get Alternative texts of the Images at Specified URLs in CSV format📜
""")
links_input = st.text_area("Enter links here", placeholder="Enter URLs here one URL per row")

# first time storing temporary dataframe to avoid any errors
if "mydataframe" not in st.session_state:
    st.session_state.mydataframe = pandas.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

if button_clicked:
    end_program()

seo_bot = Chatbot()

if st.button("Get Alt Texts"):
    # Split the string into a list of urls by a \n character
    if links_input != "":
        url_list = links_input.split("\n")

    else:
        st.info("Enter some links each link per row and press Ctrl + Enter")

    # passing urls one by one and getting response
    if len(url_list) != 0:
        # appending new links to message dictionary so that can be send to gpt-4-vision-model
        for url in url_list:
            # message dictionary to be passed to openai
            messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Pretend you're an SEO expert. Create an optimized alt text for the image. Write it as plain text no inverted commas or any heading. Don't Explain any extra thing",
                        },
                    ],
                }
            ]
            # this functions uses requests library to check if image urls are valid or not
            try:
                new_dict = {
                    "type": "image_url",
                    "image_url": {
                        "url": f"{url}",
                    },
                }
                messages[0]['content'].append(new_dict)
                print(messages)
                response = seo_bot.get_seo_optimized_words(messages)
                print(f'gett teh response {response}')
                if response:
                    valid_url_list.append(url)
                    valid_response_list.append(response)
                else:
                    invalid_url_list.append(url)
                    invalid_response_list.append("Invalid URL")
            except Exception as e:
                print(f'an error occured {e}')
                invalid_url_list.append(url)
                invalid_response_list.append("Invalid URL")

        url_list = valid_url_list + invalid_url_list

        response_list = valid_response_list + invalid_response_list

        if response_list and url_list:
            data = [url_list, response_list]
            dataframe = pandas.DataFrame(data).transpose()
            # mentioning name of columns
            dataframe.columns = ["Image URL", "Suggested alt text"]

            # displaying dataframe on screen
            st.dataframe(dataframe)

            # backup dataframe
            st.session_state.mydataframe = dataframe
            output_csv = st.session_state.mydataframe.to_csv(index=False).encode('utf-8')

    # downlaod button
    button_clicked = st.download_button("Download as CSV", data=output_csv, file_name=f"{date} - {formatted_time}.csv", mime='text/csv')

