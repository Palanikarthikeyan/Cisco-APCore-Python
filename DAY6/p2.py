import streamlit as st
import pandas as pd

name = st.text_input('Enter your name:')
#st.write(f'Hello...{name}')

age = st.slider("Select your age:",15,100,25)

if name:
    st.write(f'Hello..{name} your age is:{age}')

data = {}
data['Name']=['Ram','Tom','Leo']
data['Dept']=['sales','HR','QA']
data['City']=['City1','City2','City3']

var = st.selectbox('Choose your data:',data)
df = pd.DataFrame(data)
#st.write(df)
st.write(df[var])


uploaded_file = st.file_uploader('select your input file:',type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)


#st.audio('file.mp3')
#st.video('file.mp4')
st.image('C:\\Users\\karth\\OneDrive\\Pictures\\test1.png',caption="shapes")




    

