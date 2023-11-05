# streamlit run app.py
import streamlit as st
from io import StringIO
from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
import os

google_api_key = os.getenv("GOOGLE_API_KEY")
llm = GooglePalm(google_api_key=google_api_key, temperature=0.0)


# Create our template.
template = """
You are an experienced technical writer able to explain complicated systems in simple words.
Improve the documentation below and return it as markdown:

{text}
"""

# Create a LangChain prompt template that we can insert values to later
prompt = PromptTemplate(input_variables=["text"], template=template)

st.title("Better Documentation")
uploaded_file = st.file_uploader(
    "Choose a file",
    type="md",
    accept_multiple_files=False,
)
if uploaded_file is not None:
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    text = stringio.read()
    st.write(text)

    st.divider()

    if st.button("Improve"):
        final_prompt = prompt.format(text=text)
        with st.spinner("Doing magic..."):
            output = llm(final_prompt)
            st.write(output)
            st.divider()
            st.code(output)
