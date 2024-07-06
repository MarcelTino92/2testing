import streamlit as st
from streamlit_lottie import st_lottie
col1, col2 =st.columns([2, 3])

with col1:
    st_lottie("https://lottie.host/8c7af937-e96c-4955-a94d-199d3bea826e/oodWrMRHNo.json")

with col2:
    st.empty(height=100)
    st.header("You have completed this section")
