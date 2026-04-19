import streamlit as st
st.title("Streamlit text input")
name =  st.text_input("Enter your name : ")
st.write(f'Hello {name}')