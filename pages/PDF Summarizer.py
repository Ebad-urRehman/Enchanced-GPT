import nltk
import streamlit as st
from PyPDF2 import PdfReader
from nltk.tokenize import word_tokenize
nltk.download('punkt')
import pages.functions as functions

# default text before chat
chat_default_text = f"""👋 Aslam u Alaikum!\n
📒 Upload a PDF File and ask questions about it\n
🔍 I can search information for you\n
🙂 No need now to find specific information in a large file\n
📄 Generate Summary of a PDF file
"""

st.markdown(f"<h1 style='text-align: center;'>✨Enhanced GPT Model✨</h1>", unsafe_allow_html=True)
st.subheader("PDF Summarizer 📕")
st.info(chat_default_text)
# if pdf file uploader button is not clicked
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False
    st.session_state.old_responses = []
# total number of questions asked by user in a chat
i = 0
file = st.file_uploader("Upload a PDF file and ask Specific Questions about Information in PDF")
if file:
    # reading pdf file
    reader = PdfReader(file)
    # getting data from pdf with the help of reader.pages function
    pdf_data_list = [page.extract_text() for page in reader.pages]

    if st.button("Show PDF TEXT 👀"):
        st.session_state.button_clicked = True
        pdf_data = ""
    if st.session_state.button_clicked:
        pdf_data = ""
        # storing all pages data in a single string
        for page in pdf_data_list:
            pdf_data += page
        st.write(pdf_data)
        # giving hint to chatbot
        pdf_data += "Please provide answers about given pdf : question : "
        # finding total tokens so they can't exceed 8000
        tokenized_text = word_tokenize(pdf_data)
        tokens_pdf = len(tokenized_text)
        st.write(tokens_pdf)
        if tokens_pdf < 7000:
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

            user_input = st.text_area("", placeholder="Say a Question About PDF", key="textarea")
            if user_input != "":
                pdf_data += user_input
            tokenized_text_total = word_tokenize(pdf_data)
            total_tokens = len(tokenized_text_total)
            if total_tokens > 4096:
                st.warning("Please Enter a Question of about 700-1000 words")
            else:
                messages = [
                    {"role": "system", "content": "You are a PDF Explainer about asked questions in the given pdf text."},
                ]

                chatbot = functions.Chatbot()
                no_of_tokens = 4096
                temp = 1
                model = "gpt-4"
                response = chatbot.get_response(pdf_data, messages, no_of_tokens, temp, model)
                # it auto generates summary of PDF file
                st.header("Summary of PDF File")
                st.session_state.old_responses.append({
                    f"response_no": i,
                    f"user_input": user_input,
                    f"response": response
                })
                for old_response in st.session_state.old_responses:
                    st.info(old_response["user_input"])
                    st.write(old_response["response"])
                i = i + 1
        else:
            # if pdf file > 7000
            st.warning("Please Enter a smaller pdf file")
