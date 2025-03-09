import streamlit as st 
import pandas as pd

st.title("Streamlit Text input")

name = st.text_input("Enter your name:")

age = st.slider(f'select your age',0,100,18)

st.write(f'your age is {age}')

options = ["python",'java','c++','javascript']
choice = st.selectbox("choose your favourite language:",options)

if name:
    st.write(f"Hello, {name}!")

df = pd.DataFrame({
'first column':[1,2,3,4],
'second column': [10,20,30,40]
})
df.to_csv("sampledata.csv")

st.write(df)

uploaded_file = st.file_uploader("choose a csv file",type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)