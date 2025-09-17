import streamlit as st

st.checkbox('yes')
st.button('Click me')
st.button('press me')
st.radio('Select your option:',['Yes','No'])

st.selectbox('select your mode1:',['Model1','Model2','Model3'])

st.multiselect('choose a planet:',['Jupyter','Mars','Neptune'])

st.slider('Pick a number:',5,50)

st.select_slider('Pick a mark:',[98,99,100])
