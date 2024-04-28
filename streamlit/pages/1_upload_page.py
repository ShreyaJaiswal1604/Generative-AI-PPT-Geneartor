import streamlit as st
import pandas as pd
import time
import os
import base64

openai_api_key=os.getenv('OPENAI_API_KEY')

st.title("UPLOAD YOUR REPORT FOR ANALYSIS")

# File uploader for JSON files
uploaded_file = st.file_uploader("Upload JSON File", type=["json"])

if uploaded_file is not None:
    try:
        json_data = pd.read_json(uploaded_file)
        st.write(json_data)

        st.write(f"Please verify json file and click save to proceed")

        if st.button("Save the file"):
            with st.spinner('Saving and moving to next page'):
                with open(f"./tmp/{uploaded_file.name}", "w") as file:
                    file.write(uploaded_file.getvalue().decode("utf-8"))
                st.switch_page("pages/2_ppt_generator_bot.py")

    except Exception as e:
        # st.write("Error: ", e)
        st.error("Please upload a valid JSON file")
        # del uploaded_file

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
   
side_bg_ext = '../media/images/img-08.jpeg'

sidebar_bg(side_bg_ext)