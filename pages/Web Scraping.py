import requests
import streamlit as st
import utils.scraping_utils as utils


with st.sidebar :
    format = st.radio('Select file format to download', ['md', 'html'])
    st.info(format)

st.header('🔍🌐Web Scraping📜')
url = st.text_input('Enter Url here')

st.info('Example url : https://www.productreview.com.au/listings/shopify')

if st.button('Scrape'):
    response = utils.scrape_website(url, format)
    save_file_name = url.replace('//', '').replace('/', '')
    
    if st.download_button(
        label="Download File",
    data=response.text, 
    file_name=f'{save_file_name}.{format}',  
    mime="text/plain"  
    ):    

        st.info(f'File {save_file_name}.{format} saved to disk')
