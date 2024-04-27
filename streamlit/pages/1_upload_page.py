import streamlit as st
import pandas as pd

import os

openai_api_key=os.getenv('OPENAI_API_KEY')


def main():
    st.title("UPLOAD YOUR REPORT FOR ANALYSIS")

    # File uploader for JSON files
    uploaded_file = st.file_uploader("Upload JSON File", type=["json"])

    if uploaded_file is not None:
        # Read JSON file
        json_data = pd.read_json(uploaded_file)

        # Display as table
        st.write("### JSON Data")
        st.write(json_data)

        # Add button to move to chatbot application
        if st.button("Go to PPT Generator Bot"):
            # Redirect to chatbot application
            st.write("Redirecting to bot Application.....")
            # Add the hyperlink to your chatbot application
            st.switch_page("pages/2_ppt_generator_bot.py")


if __name__ == "__main__":
    main()