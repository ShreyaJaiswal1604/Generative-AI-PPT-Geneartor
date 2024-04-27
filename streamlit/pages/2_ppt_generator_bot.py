import streamlit as st
import pandas as pd

import os

openai_api_key=os.getenv('OPENAI_API_KEY')

st.session_state.messages = None

st.header(":page_with_curl: Your PPT Generator Bot ")

st.subheader('Hi There, Go ahead and ask your query!', divider='rainbow')