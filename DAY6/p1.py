# import streamlit
# streamlit.title('Welcome')


import streamlit as st
st.title('Welcome')
st.header('This is sample headline')
st.write('This is test message')
st.write('list of records from db')

import pandas as pd
df = pd.DataFrame({'K1':[10,20,30,40,50],'K2':[100,200,300,400,500]})

st.write('sample data from pandas')
st.write(df)

import numpy as np
df1 = pd.DataFrame(np.random.randn(20,3),columns=['A','B','C'])
st.write(df1)
st.line_chart(df1)