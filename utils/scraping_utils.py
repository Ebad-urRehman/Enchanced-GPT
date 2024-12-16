from datetime import date
import os
import requests

def scrape_website(url):
    url = f'https://r.jina.ai/{url}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            print(f'Fail to fetch response status code {response.status_code}')
    except Exception as e:
        print('Error : \n {e}')
    

def save_file_as_md(save_file_name, response):
    current_date = date.today().strftime("%d-%m-%Y")
    print(type(current_date))
    save_path = f'files/Scraping/{current_date}'

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    with open(f'{save_path}/{save_file_name}.md', 'w') as file:
        file.write(response.text)