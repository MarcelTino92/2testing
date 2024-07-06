import streamlit as st
from streamlit_lottie import st_lottie
#col1, col2 =st.columns([1, 3])

col1,col2=st.columns([1, 1])

with col1:
  st_lottie("https://lottie.host/8c7af937-e96c-4955-a94d-199d3bea826e/oodWrMRHNo.json")

with col2:
  st.markdown(
        """
        <style>
        .centered-title-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 30vh;
        }
        .centered-title {
            font-size: 32px;
            font-weight: bold;
            white-space: nowrap;
            margin: 10px 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
  st.markdown(
        '''
        <div class="centered-title-container">
            <div class="centered-title"> Answers are recorded for this section</div>
        </div>
        ''', 
        unsafe_allow_html=True
    )

st.title("*Please close this Tab*")
