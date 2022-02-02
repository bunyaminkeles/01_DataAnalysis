import streamlit as st
import pandas as pd
import numpy as np
import datetime
from PIL import Image

st.title('Hello World')
st.text('Bu bir text')
st.markdown('`This is a markdown text`')
st.header('This is a header')
st.subheader('Subheader hurra!')

st.success('Congrats!')
st.info('Warning!')
st.error('Dang!')

st.help(range)
st.write('this is a text written witherite func')

img = Image.open('cat.jpg')
st.image(img, caption='Cattie', use_column_width=True)
st.video('https://www.youtube.com/watch?v=DHfRfU3XUEo')

if st.checkbox('Hide and Seek'):
    st.write('Seek')
status = st.radio("Who is your favourite instructor?", ("Edward","Orion","Johnson","Steve"))

st.write(f'your favotrite clolor is{status}')

#Button
if st.button('Unnecessary button'):
	st.success('big brain move')
	
#Selectbox
selected_number = st.selectbox('Select a number', [0, 1, 2, 3, 4, 5])
if selected_number == 0:
	st.write('No cats for you -.-')
else:
	st.write(f'I am sending you {selected_number} cats')

multi_select = st.multiselect('Select multiple numbers', [0, 1, 2, 3, 4, 5])
if len(multi_select) > 0:
	st.write(f'you selected {multi_select}')
else:
	st.write('You didnt select anything')
options = st.slider('Select a number', 0.0, 5.0, 3.0, 0.1)

name = st.text_input('Enter your name')
if st.button('Submit'):
	st.write(f'Hello, {name.title()}')

txt = st.text_area('Enter a message', 'Type your message right here...')
st.date_input('Date', datetime.datetime.now())
