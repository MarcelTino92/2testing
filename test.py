import streamlit as st
import streamlit.components.v1 as components

# Define the URL you want to allow

# Create the HTML for CSP and iframe
html_code = f"""
    <head>
  <meta http-equiv="refresh" content="0; URL=https://huggingface.co/spaces/giswqs/Streamlit" />
</head>
<body>
</body>
"""

# Display the HTML code
components.html(html_code, height=650)
