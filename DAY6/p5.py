import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

prompt= ChatPromptTemplate.from_messages([
    ("system","Your are a helpful AI assistant"),("user","Question:{question}")
])
llm = Ollama(model="gemma:2b")
output = StrOutputParser()
chain = prompt|llm|output

st.title('Langchain Demo with Gemma2 model')

input_text=st.text_input('Enter your query?')

if input_text:
    st.write(chain.invoke({'question':input_text}))
