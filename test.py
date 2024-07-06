import streamlit as st
from streamlit_lottie import st_lottie
#col1, col2 =st.columns([1, 3])

col1,col2=st.columns([1, 2])

with col1:
  st_lottie("https://lottie.host/8c7af937-e96c-4955-a94d-199d3bea826e/oodWrMRHNo.json")

with col2:
  st.markdown(
        """
        <style>
        .centered-title {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
            font-size: 48px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
  st.markdown('<div class="centered-title">Please close the Tab</div>', unsafe_allow_html=True)
