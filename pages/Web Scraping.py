import requests
import streamlit as st
import utils.scraping_utils as utils


url = st.text_input('Enter Url here')

st.info('Example url : https://www.productreview.com.au/listings/shopify')

if st.button('Scrape'):
    response = utils.scrape_website(url)
    save_file_name = url.replace('//', '').replace('/', '')
    utils.save_file_as_md(save_file_name, response)
    

    st.info(f'File {url}.md saved to disk')
