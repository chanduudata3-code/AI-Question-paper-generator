import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils import generate_pdf

st.title("Download Question Paper")

if "questions" not in st.session_state:
    st.warning("Generate questions first.")
else:

    questions = st.session_state["questions"]

    pdf_file = generate_pdf(questions)

    with open(pdf_file, "rb") as f:
        st.download_button(
            "Download PDF",
            f,
            file_name="question_paper.pdf"
        )