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


st.image('../images/img-04.jpeg', caption='Let\'s get started', width=600)

def sidebar_bg(side_bg):

   side_bg_ext = 'png'

   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
   
side_bg_ext = '../images/img-08.jpeg'

sidebar_bg(side_bg_ext)