import streamlit as st

st.number_input('Pick a number:',0,20)
st.text_input('Email')
st.date_input('Travelling date')
st.time_input('Meeting time')
st.text_area('Description')
st.file_uploader('upload a photo:')
st.color_picker('Select your favorite color')
