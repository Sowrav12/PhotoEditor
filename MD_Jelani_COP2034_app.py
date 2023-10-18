# implemented all the necessary libraries 
# connected filter.py to webapp.py

import streamlit as st 
import numpy as np
from PIL import Image
import cv2 
from filters import apply_filter
import os 

# implement a css file 

st.markdown(
    f'''
    <style> 
        {' '.join(open('style.css').readlines())} 
    </style> 
    ''',
    unsafe_allow_html = True, 
)

# create a title and short description of the web application 

st.sidebar.title('Photo Editor Application')
st.sidebar.write('This is a basic photo editor that consists of 5 filters that users can use and change the intensity of the filter. Filters are Gray Image, Black and White, Pencil Sketch, Blur Effect, and Inverted') 

# imported the logo and aligned everything 

logo = 'logo.png'
col1, col2 = st.columns([3, 1])
with col1: 
    st.markdown('<h1>MD Golam Jelani</h1>', unsafe_allow_html=True)
    st.markdown('<h1>Final Project COP 2034</h1>', unsafe_allow_html=True)
    st.markdown('<h1>05/03/2023</h1>', unsafe_allow_html=True)
    st.markdown('--'*50)
with col2: 
    st.image(logo, width=100)
    
# created a upload button 

image = st.file_uploader('Drag and drop file here', type = ['jpg', 'png', 'jpeg'])

# created radio buttons for the filters 

if image: 
    img = Image.open(image)
    filters = st.sidebar.radio('Filters', ('None', 'Gray Image', 'Black and White', 'Pencil Sketch', 'Blur Effect', 'Invert'), key = 'filter')

    if filters != 'None':
        intensity = st.sidebar.slider('Intensity', 0.0, 1.0, 0.7, 0.01)
        filtered_img = apply_filter(filters, img, intensity)
        st.image([img, filtered_img], caption=['Original Image', 'Filtered Image'], width=300) # this set both images side by side 
        
        # placed the edited images in a folder --> output 

        filename = f"{filters.replace(' ', '_')}_{image.name}"
        filtered_img.save(os.path.join('output', f'{filename}.png'), 'PNG')

        with open(os.path.join('output', f'{filename}.png'), 'rb') as f:
            image = f.read()
            st.download_button(label='Download filtered image', data=image, file_name=filename)