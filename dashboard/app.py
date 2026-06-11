import streamlit as st

st.set_page_config(page_title="Data Platform", layout="wide")

st.title("📊 Data Analysis Dashboard")

st.write("If you can see this → Streamlit is working 🚀")

data = [100, 200, 150, 300]

st.line_chart(data)
