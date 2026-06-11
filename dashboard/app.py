import streamlit as st
import requests

st.title("📊 Data Dashboard (Connected to API)")

# 调用你的 FastAPI
res = requests.get("http://localhost:10000/data")
data = res.json()

st.write("📦 API Data:", data)

st.subheader("Sales")
st.line_chart(data["sales"])

st.subheader("Profit")
st.bar_chart(data["profit"])
