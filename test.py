import streamlit as st
from streamlit_lottie import st_lottie
col1, col2 =st.columns(2)

with col1:
    st_lottie("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

with col2:
    st.write("The file is shown")
