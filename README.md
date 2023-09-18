# Enchanced-GPT

### ⚪ It is a College project for project exhibition

I decided to make a project of chatbot which have features like Chatgpt as well as it can speak to you and hear your voice, as well as read PDF files and give answers about questions ask about that pdf file.

Here is a Breif Detail of How it works

## 🔵 How it works

Enhanced Chatbot Project is maade in Python Library streamlit(for interface). Here is a breif overview of how it works

# Home Page
Home page is built in file Home.py. It first checks if the user is login or not by checking if the file json.data named as account.json exists.
![image](https://github.com/Ebad-urRehman/Enchanced-GPT/assets/125203236/7dc0ed2b-e8e7-4dc1-8752-1ad40b8149cb)

If it is not it takes necessary Information and sign for signing up the user.

![image](https://github.com/Ebad-urRehman/Enchanced-GPT/assets/125203236/18234564-d5ed-41ef-8c57-904489a3986d)

When the sign in process complete user data is store in a dataframe then in the file account.json


![image](https://github.com/Ebad-urRehman/Enchanced-GPT/assets/125203236/f4fd52d0-720f-4e5a-8af6-a289a9785cd3)

Now the file exists thus sign in process is complete and user is now signed in.

🙂 ### User can chat now
![image](https://github.com/Ebad-urRehman/Enchanced-GPT/assets/125203236/c30581c9-6a86-4066-8c4e-fad3401e68de)


# Chat History.py
In Main file History Dataframe is used to save history chats.
It can do so by storing this record in a file named as DD-MM-YY.json format.
Time module is used to get current day, mounth and year.
then the history dataframe is stored in file DD-MM-YY.json file

## Chat history.py get list of these files get there data and display them in form of radio options in sidebar.

![image](https://github.com/Ebad-urRehman/Enchanced-GPT/assets/125203236/4ccc34b3-69ae-40f0-a194-a3c436512b13)

# PDF Reader.py
This file has a browse button to upload a PDF file and ask questions about that file

# The Reality of Backend
I use open ai api key which is not for free.
But if you make a new account you can get 5$ free trial which you can use to build your own chatbot.

A chatbot file has been created in File 🗄️ Functions.py in which API key is given in constructor and a function called chatbot response is used to get response from chatgpt 3.5 turbo version you can see the details in code.

## Important concepts

## 🔴 Tokens
Here is a breif explanation of tokens

![image](https://github.com/Ebad-urRehman/Enchanced-GPT/assets/125203236/07c6aa06-d617-49b3-a32f-fadf3c7ce045)

You can say tokens are words for chatbot
see details here : https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them

## 🔴 Temprature
### Temprature ranges from 0 to 1
High temperature: The model is more likely to produce a variety of words and generate novel, imaginative responses.
Low temperature: The model is more likely to stick to what it has learned and provide more conservative, probable responses.

### How should I set the temperature parameter?
Lower values for temperature result in more consistent outputs, while higher values generate more diverse and creative results. Select a temperature value based on the desired trade-off between coherence and creativity for your specific application.

### ⏭️ This Project is Incomplete for now if there are any suggestions comment down please
