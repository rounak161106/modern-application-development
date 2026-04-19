import streamlit as st
import numpy as np
import pandas as pd


st.title("Hello Streamlit")

st.write("Here is the DataFrame")

df = pd.DataFrame({
    "Name" : ["Rounak", "Tanya", "Jay"], 
    "Age" : [18,19,15]
})
df.to_csv("data.csv")
st.write(df)

# ================================================================
st.write("Here is the chart data")
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)

st.line_chart(chart_data)