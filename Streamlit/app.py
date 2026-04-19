import streamlit as st
import numpy as np
import pandas as pd


st.title("Hello Streamlit")

st.write("Here is the DataFrame")

df = pd.DataFrame({
    "Name" : ["Rounak", "Tanya", "Jay"], 
    "Age" : [18,19,15]
})

st.write(df)

