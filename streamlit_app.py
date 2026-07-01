
#   streamlit run streamlit_app.py

import streamlit as st
from llm_core import ask

st.title("Ask the LLM")
st.write("Type any question below and click **Ask**.")

question = st.text_area(
    label="Your question",
    height=150,
    placeholder="e.g. What is machine learning?"
)

if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please type a question first.")

    else:
        with st.spinner("Thinking..."):
            answer = ask(question)

        st.markdown("### Answer")
        st.write(answer)
