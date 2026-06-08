import streamlit as st

st.set_page_config(
    page_title="TRO Pro Resume Generator",
    layout="wide"
)

st.title("TRO Pro Resume Generator")

st.write(
    "Resume PDF and Cover Letter PDF Generator"
)

jd = st.text_area(
    "Paste Job Description",
    height=250
)

if st.button("Analyze"):
    if jd.strip():
        st.success("JD received successfully.")
    else:
        st.warning("Please paste a Job Description.")
