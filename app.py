import streamlit as st

from pdf_builder import create_resume_pdf


st.set_page_config(
    page_title="TRO Pro Resume Generator",
    layout="wide"
)

st.title("TRO Pro Resume Generator")

candidate_name = st.text_input(
    "Candidate Name",
    value="Anubhav Tripathi"
)

target_role = st.text_input(
    "Target Role"
)

summary = st.text_area(
    "Professional Summary"
)

if st.button("Generate Resume PDF"):

    create_resume_pdf(
        "generated_resume.pdf",
        candidate_name,
        target_role,
        summary,
    )

    with open(
        "generated_resume.pdf",
        "rb"
    ) as file:

        st.download_button(
            label="Download Resume PDF",
            data=file,
            file_name="Resume.pdf",
            mime="application/pdf",
        )
