import streamlit as st
from utils import extract_text_from_pdf, generate_questions

# Page config
st.set_page_config(page_title="Generate Questions", page_icon="📄")

# Title
st.title("📄 Generate Questions from PDF")

st.write("Upload your study material and generate exam questions automatically.")

# Upload section
uploaded_file = st.file_uploader("Upload PDF File", type=["pdf"])

# Marks selection (responsive layout)
col1, col2, col3 = st.columns(3)

with col1:
    two = st.number_input("2 Marks Questions", min_value=1, max_value=20, value=5)

with col2:
    five = st.number_input("5 Marks Questions", min_value=1, max_value=20, value=3)

with col3:
    ten = st.number_input("10 Marks Questions", min_value=1, max_value=20, value=2)

# Generate button
if st.button("🚀 Generate Questions"):

    if uploaded_file is None:
        st.warning("⚠️ Please upload a PDF file first.")
    else:
        # Extract text
        with st.spinner("📖 Reading PDF..."):
            text = extract_text_from_pdf(uploaded_file)

        # Generate questions
        with st.spinner("🤖 Generating questions..."):
            questions = generate_questions(text, two, five, ten)

        # Store in session
        st.session_state["questions"] = questions

        # Success message
        st.success("✅ Questions generated successfully!")

        # Preview small snippet
        st.subheader("🔍 Quick Preview")

        for i, q in enumerate(questions[:5], 1):
            st.write(f"{i}. ({q['marks']} Marks) {q['question']}")

        st.info("👉 Go to 'Preview Questions' page for full view.")