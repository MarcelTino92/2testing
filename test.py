import streamlit as st
from streamlit_lottie import st_lottie
col1, col2 =st.columns([1, 3])

with col1:
    st_lottie("https://lottie.host/8c7af937-e96c-4955-a94d-199d3bea826e/oodWrMRHNo.json")

with col2:
    long_title ="AI Question-Part1 is completed"
    # Apply CSS styling using st.markdown
    st.markdown(f"""<style>
    .title-container {{
        width: 400px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;  /* Prevent additional whitespace within the title */
    }}
    </style>
    <div class="title-container">
    <h1>{long_title}</h1>
    </div>""", unsafe_allow_html=True)
    st.title("*Please close this Tab*")
