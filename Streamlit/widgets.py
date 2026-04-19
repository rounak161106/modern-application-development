import streamlit as st
import pandas as pd

st.title("Streamlit Demo")
name =  st.text_input("Enter your name : ")
st.write(f'Hello {name}')

#add slider to take age as input
age = st.slider("Select your age : ",10,80,15)
st.write(f'Your age is {age}')

#add select options
options = ["Python", "Java", "C++", "Ruby"]
choice = st.selectbox("Select your favorite programming language : ", options)
st.write("You selected", choice)

uploaded_file = st.file_uploader("Choose a csv file ", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)