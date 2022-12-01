import streamlit as st
import pandas as pd

st.write("""
# My First App
Hello World*
""")

df = pd.read_csv("mydata.csv")
st.line_chart(df)
