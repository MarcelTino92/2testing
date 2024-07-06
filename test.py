import streamlit as st
from streamlit_lottie import st_lottie
col1, col2 =st.columns([2, 3])

with col1:
    st.markdown("<img src="https://lottie.host/8c7af937-e96c-4955-a94d-199d3bea826e/oodWrMRHNo.json" width='100' style='display: block; margin: 0 auto;'>" , unsafe_allow_html=True)
    #st_lottie("https://lottie.host/8c7af937-e96c-4955-a94d-199d3bea826e/oodWrMRHNo.json")

with col2:
    title_alignment=
        """
        <style>
        #the-title {
          text-align: center
        }
        </style>
        """
    st.markdown(title_alignment, unsafe_allow_html=True)
