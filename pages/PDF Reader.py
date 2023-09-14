import nltk
import streamlit as st
# import nltk
from PyPDF2 import PdfReader
from nltk.tokenize import word_tokenize
nltk.download('punkt')
import functions
st.title("PDF Reader")

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False
    st.session_state.old_responses = []
i = 0
file = st.file_uploader("Upload a PDF file and ask Specific Questions about Information in PDF")
if file:
    reader = PdfReader(file)
    # all_pages = [reader.pages[i] for i in range(len(reader.pages))]
    pdf_data_list = [page.extract_text() for page in reader.pages]

    if st.button("Show PDF TEXT"):
        st.session_state.button_clicked = True
        pdf_data = ""
    if st.session_state.button_clicked:
        pdf_data = ""
        for page in pdf_data_list:
            pdf_data += page
            # st.write(page)
        st.write(pdf_data)
        pdf_data += "Please provide answers about given pdf : question : "
        tokenized_text = word_tokenize(pdf_data)
        tokens_pdf = len(tokenized_text)
        st.write(tokens_pdf)
        if(tokens_pdf < 7000):
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
            # st.text(pdf_data)
            tokenized_text_total = word_tokenize(pdf_data)
            total_tokens = len(tokenized_text_total)
            if total_tokens > 8000:
                st.warning("Please Enter a Question of about 700-1000 words")
            else:
                messages = [
                    {"role": "system", "content": "You are a PDF Explainer about asked questions in the given pdf text."},
                ]

                chatbot = functions.Chatbot()
                response = chatbot.get_response(pdf_data, messages)
                st.header("Summary of PDF File")
                st.session_state.old_responses.append({
                    f"response_no": i,
                    f"user_input": user_input,
                    f"response": response
                })
                for old_response in st.session_state.old_responses:
                    st.info(old_response["user_input"])
                    st.write(old_response["response"])
                    # st.info(user_input)
                    # st.write(response)
                i = i + 1
        else:
            st.warning("Please Enter a smaller pdf file")
