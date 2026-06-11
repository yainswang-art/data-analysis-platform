import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Platform", layout="wide")

st.title("📊 Data Analysis Platform")

st.write("If you can see this → Dashboard is working 🚀")

data = pd.DataFrame({
    "sales": [100, 200, 150, 300],
    "profit": [20, 50, 30, 80]
})

st.subheader("Sales")
st.line_chart(data["sales"])

st.subheader("Profit")
st.bar_chart(data["profit"])
