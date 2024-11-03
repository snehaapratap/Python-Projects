import streamlit as st
import replicate
import os
import requests
from PIL import Image
from io import BytesIO

# Set up your Replicate API key (optionally from environment variable)
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")  # You can store your API key in an environment variable

if REPLICATE_API_TOKEN is None:
    st.error("Replicate API token not found. Please set it in your environment.")
    st.stop()

# Authenticate with Replicate using the API token
replicate.Client(api_token=REPLICATE_API_TOKEN)


if 'image_url' not in st.session_state:
    st.session_state['image_url'] = None

with st.sidebar:
    st.title('AI Image Generator')
    st.header("Prompt and Options")
    prompt = st.text_area('Enter a prompt to generate an image', height=50)
    seed = st.checkbox('Use Random Seed', value=True)
    if seed:
        random = st.slider('Random Seed', 0, 1000, 435)
    else:
        random = None
    output_quality = st.slider('Output Quality', 50, 100, 80)
    col1, col2 = st.columns([1, 1])
    gen = col1.button('Generate Image')

if gen and prompt:
    with st.spinner('Generating image...'):
        try:
            input_data = {
                "prompt": prompt,
                "aspect_ratio": '3:2',  
                "quality": output_quality  
            }

            if seed is not None:
                input_data["seed"] = seed

            output = replicate.run(
                "black-forest-labs/flux-schnell",  
                input=input_data  
            )

            st.session_state['image_url'] = output[0] 

        except Exception as e:
            st.error(f"An error occurred: {e}")

if st.session_state['image_url']:
    st.image(st.session_state['image_url'], caption='Generated Image')

    response = requests.get(st.session_state['image_url'])
    image = Image.open(BytesIO(response.content))

    img_buffer = BytesIO()
    image.save(img_buffer, format="JPEG") 
    img_buffer.seek(0)
    with col2:
        st.download_button(
            label="Download Image",
            data=img_buffer,
            file_name="generated_image.jpg",
            mime="image/jpeg"
        )
