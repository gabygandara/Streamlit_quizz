import streamlit as st
st.title("Application Quiz")

# Input question 1
st.subheader("Question 1 : ")
with st.form("question1"):
    reponse1 = st.text_input(" Quel est le ballon d'or 2023? ")
    button = st.form_submit_button("Confirm")

if button:
    if reponse1.lower() == "Messi":
        st.write("Right answer ! ")
