import streamlit as st
st.title("Streamlit text input")
name =  st.text_input("Enter your name : ")
st.write(f'Hello {name}')

#add slider to take age as input
age = st.slider("Select your age : ",10,80,15)
st.write(f'Your age is {age}')