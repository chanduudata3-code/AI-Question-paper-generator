import streamlit as st
from utils import generate_questions

st.title("Generate Questions")

topic = st.text_input("Enter Topic")

col1, col2, col3 = st.columns(3)

with col1:
    two = st.number_input("2 Marks", 0, 20, 5)

with col2:
    five = st.number_input("5 Marks", 0, 20, 3)

with col3:
    ten = st.number_input("10 Marks", 0, 20, 2)

if st.button("Generate Questions"):

    questions = generate_questions(topic, two, five, ten)

    st.session_state["questions"] = questions

    st.success("Questions Generated! Go to Preview Page.")