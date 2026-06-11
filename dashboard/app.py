import streamlit as st

st.title("📊 Data Analysis Dashboard")

st.write("Welcome to your deployed analytics platform 🚀")

data = {"sales": [100, 200, 150, 300]}

st.line_chart(data)
