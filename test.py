import streamlit as st
from streamlit_lottie import st_lottie
col1, col2 =st.columns([1, 3])

with col1:
    st_lottie("https://lottie.host/8c7af937-e96c-4955-a94d-199d3bea826e/oodWrMRHNo.json")

with col2:
    long_title ="AI Question-Part1 is completed"
    st.title(f"""<nobr>{long_title}</nobr>""", unsafe_allow_html=True)
    st.title("*Please close this Tab*")
