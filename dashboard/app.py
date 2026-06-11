import os
import streamlit as st

st.write("📍 CURRENT FILE PATH:")
st.code(os.path.abspath(__file__))

print("🔥 RUNNING THIS FILE")

import streamlit as st
st.write("🔥 THIS IS THE ACTIVE STREAMLIT FILE")
