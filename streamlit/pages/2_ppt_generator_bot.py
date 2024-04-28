import streamlit as st
from openai import Client
import time
from PIL import Image
from openai import OpenAI
import io
import os

openai_api_key=os.getenv('OPENAI_API_KEY')
# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def convert_file_to_png(file_id, write_path):
    data = client.files.content(file_id)
    data_bytes = data.read()
    with open(write_path, "wb") as file:
        file.write(data_bytes)

def main():
    st.title("PPT Generator Bot")

    # Get user input for insight query
    insight_query_one = st.text_input("Enter Insight Query")

    if st.button("Generate PowerPoint Presentation"):
        # Create file in OpenAI
        file = client.files.create(
            file=open("../NotRealCorp_financial_data.json", "rb"),
            purpose='assistants'
        )

        # Create assistant with the file
        assistant = client.beta.assistants.create(
            name="Data visualizer",
            description="Your assistant description here...",
            model="gpt-4-1106-preview",
            tools=[{"type": "code_interpreter"}],
            tool_resources={
                "code_interpreter": {
                    "file_ids": [file.id]
                }
            }
        )

        # Create a thread to communicate with the assistant
        thread = client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{insight_query_one}",
                    "attachments": [
                        {
                            "file_id": file.id,
                            "tools": [{"type": "code_interpreter"}]
                        }
                    ]
                }
            ]
        )

        # Run the assistant
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id
        )

        # Display a loading spinner while waiting for the plot to be created
    with st.spinner(text='Assistant still working...'):
        while True:
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            try:
                # Check if the image has been created
                messages.data[0].content[0].image_file
                # Sleep to make sure the run has completed
                time.sleep(5)
                st.success('Plot created!')
                break
            except:
                # If image has not been created, continue showing the spinner
                continue

        # # Poll assistant to check if process is completed
        # while True:
        #     messages = client.beta.threads.messages.list(thread_id=thread.id)
        #     try:
        #         # Check if image has been created
        #         messages.data[0].content[0].image_file
        #         # Print message once plot is created
        #         st.success('Plot created!')
        #         break
        #     except:
        #         # Print message while assistant is still working
        #         st.warning('Assistant still working...')
        #         time.sleep(10)

        # Display the output image to the user
        for message in messages.data:
            if message.content[0].type == "image_file":
                file_id = message.content[0].image_file.file_id
                plot_summary = message.content[1].text.value
                image_bytes = client.files.content(file_id).read()
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image, caption=plot_summary, use_column_width=True)

if __name__ == "__main__":
    main()

# st.session_state.messages = None

# st.header(":page_with_curl: Your PPT Generator Bot ")

# st.subheader('Hi There, Go ahead and ask your query!', divider='rainbow')