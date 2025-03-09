'''
Introduction to Streamlit: 

================================
Streamlit is open-source app framework for machine learning and data science projects.
It allows users to create web applications with simple python scripts



'''



import streamlit as st
import pandas as pd
import numpy as np


## Title of the application

st.title("Hello Streamlite web app")

## Display a simple text

st.write("This is simple text")

## create a simple DataFrame

df = pd.DataFrame({
'first column':[1,2,3,4],
'second column': [10,20,30,40]

})

## Display DataFrame
st.write("Here is the dataframe")
st.write(df) 

## create a line chart
chart_data= pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(chart_data)