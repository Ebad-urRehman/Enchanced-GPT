import streamlit as st

# Create a sidebar for navigation
navigation = st.sidebar.radio("Navigation", ["Chat 1", "Chat 2", "Chat 3"])

# Define the content for each Chat
if navigation == "Chat 1":
    st.title("Chat 1")
    st.header("Date : ")
    st.subheader("User prompt")
    st.text("chatbot response")
elif navigation == "Chat 2":
    st.title("Chat 2")
    st.header("Date : ")
    st.subheader("User prompt")
    st.text("chatbot response")
elif navigation == "Chat 3":
    st.title("Chat 3")
    st.header("Date : ")
    st.subheader("User prompt")
    st.text("chatbot response")

