import streamlit as st

st.title("Preview Question Paper")

if "questions" not in st.session_state:
    st.warning("Generate questions first.")
else:

    questions = st.session_state["questions"]

    for i, q in enumerate(questions, 1):

        st.markdown(
            f"""
            **{i}. ({q['marks']} Marks)**  
            {q['question']}
            """
        )