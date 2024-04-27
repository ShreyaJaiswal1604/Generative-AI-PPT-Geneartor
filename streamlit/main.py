import streamlit as st
import base64
from dotenv import load_dotenv
load_dotenv()


# Set page title and icon
st.set_page_config(
    page_title="PPT-Generator Home",
    page_icon="🤖",
    initial_sidebar_state='collapsed'
)

# Main title
st.title("Welcome to PPT-Generator 🌟")
# Description
st.write("This is a PPT-Generator  application designed to assist you creating PPTs by visualizing your reports and your query.")
