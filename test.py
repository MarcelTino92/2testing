import streamlit as st
import streamlit.components.v1 as components

def display_error_message(lottie_url):
    """Displays an error message with an optional Lottie animation."""

    st.markdown("""<body style="background-color: #f5f5f5; font-family: Arial, sans-serif;">""", unsafe_allow_html=True)

    # Header
    st.markdown("""<header style="display: flex; align-items: center;">""", unsafe_allow_html=True)

    # Lottie animation (if provided)
    if lottie_url:
        st.components.v1.iframe(lottie_url, width=250, height=250, style="margin-right: 20px;")

    # Text content
    st.markdown("""<div>
                   <h1 style="font-size:25px;"><em>The Page you have used has expired.</em></h1>
                   <h1 style="font-size:25px;"><em>Please close the tab</em></h1>
                 </div>
                 </header>""", unsafe_allow_html=True)

# Example usage (assuming you have a Lottie animation URL)
lottie_url = "https://lottie.host/8c7af937-e96c-4955-a94d-199d3bea826e/oodWrMRHNo.json"  # Replace with your actual URL
display_error_message(lottie_url)
