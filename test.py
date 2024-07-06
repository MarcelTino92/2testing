import streamlit as st
from streamlit_lottie import st_lottie
col1, col2 =st.columns([2, 3])

with col1:
    st_lottie("https://lottie.host/8c7af937-e96c-4955-a94d-199d3bea826e/oodWrMRHNo.json")

with col2:
    st.markdown("""<style>
        .col2-content {
            text-align: left;  /* Change to 'right' for right-alignment */
        }
    </style>""", unsafe_allow_html=True)

    with st.container(class_="col2-content"):
        st.empty()  # Optional: Add some space before the title
        st.title("You have completed this section")
