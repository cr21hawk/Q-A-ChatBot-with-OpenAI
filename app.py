import streamlit as st
import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import openai

_ = load_dotenv(find_dotenv())

# Langsmith tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

# prompt template
prompt = ChatPromptTemplate(
    [
        ('system', 'You are a helpfull assitant. Please respond to user queries'),
        ('user', 'question: {question}')
    ]
)


def generate_response(api_key, llm, temperature, max_tokens, question):
    openai.api_key = api_key
    llm = ChatOpenAI(model=llm, api_key= api_key, temperature= temperature, max_tokens=max_tokens)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke(question)
    return answer

# Title of the app
st.title("Q&A Chatbot With OpenAI")

# Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")

# Drop down to select a various OpenAI models
llm = st.sidebar.selectbox("Select an OPEN AI model",["gpt-4o","gpt-4-turbo","gpt-4"])

# Adjust response parameter
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Main interface for user input
st.write("Hey! Nice to meet you. I am ready to help you...")
user_input = st.text_input("You:")

if user_input:
    response = generate_response( 
        api_key=api_key, 
        llm=llm, 
        temperature=temperature, 
        max_tokens= max_tokens,
        question=user_input
        )
    st.write(response)
else:
    st.write("Please provide a question to answer...")