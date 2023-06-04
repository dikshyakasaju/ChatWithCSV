import streamlit as st 
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd
from pandasai import PandasAI

load_dotenv()


#openai_api_key = os.getenv("OPENAI_API_KEY")

OPENAI_API_KEY = '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'

def chat_with_csv(df, query):
    llm = OpenAI(api_token=OPENAI_API_KEY, temperature = 0.1)
    pandas_ai = PandasAI(llm)
    result = pandas_ai.run(df, prompt=query)
    print(result)
    return result

st.set_page_config(layout='wide')

st.title("Chat with CSV 🗂️")

input_csv = st.file_uploader("Upload your CSV file", type=['csv'])

if input_csv is not None:

        col1, col2 = st.columns([1,1])

        with col1:
            st.success("CSV Uploaded Successfully")
            data = pd.read_csv(input_csv)
            st.dataframe(data, use_container_width=True)

        with col2:

            st.info("Chat Below")
            
            input_text = st.text_area("Enter your query")

            if input_text is not None:
                # If user presses the button
                if st.button("Chat with CSV"):
                    with st.spinner('Processing'):
                         #st.info("Your Query: " + input_text)
                        result = chat_with_csv(data, input_text)
                        st.success(result)

