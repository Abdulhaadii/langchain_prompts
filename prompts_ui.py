from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Initialize model
model = ChatOpenAI(model="gpt-3.5-turbo")

# UI
st.header("Research Tool")

user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    if user_input:
        result = model.invoke(user_input)
        st.write(result.content)
    else:
        st.warning("Please enter some text.")
