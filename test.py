import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.bottom_container import bottom
#col1, col2 =st.columns([1, 3])  
col1,col2=st.columns([1, 2])

with col1:
  st.markdown('<div class="center-content">', unsafe_allow_html=True)
  st_lottie("https://lottie.host/a9e02ba9-9254-437b-8dca-493958122b8c/x9shcw0SXx.json")
  st.markdown('</div>', unsafe_allow_html=True)

with col2:
  st.markdown(
        """
        <style>
        .centered-title-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 15vh;
        }
        .centered-title {
            font-size: 18px;
            font-weight: bold;
            white-space: nowrap;
            font-style: italic;
            margin: 10px 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
  st.markdown(
        '''
        <div class="centered-title-container">
            <div class="centered-title">  Redirecting you to a new page. Please close the Tab</div>
        </div>
        ''',
        unsafe_allow_html=True
    )
with bottom():
  st.write("This app is prepared by SRI")


