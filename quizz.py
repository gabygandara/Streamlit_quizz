import streamlit as st
st.title("Application Quiz")

st.subheader("Question 1 : ")
with st.form("question1"):
    reponse1 = st.text_input("Quel est le ballon d'or 2023? ")
    button = st.form_submit_button("Confirm")
if button:
    if reponse1.lower() == "Messi":
        st.write("Excellente réponse ! ")
    else:
        st.write("Mauvaise réponse ! ")

st.subheader("Question 2 : ")
with st.form("question2"):
    reponse2 = st.text_input("Quel acteur américain a remporté l'oscar du meilleur acteur 2023? ")
    button = st.form_submit_button("Confirm")
if button:
    if reponse2.lower() == "Brendan Fraser":
        st.write("Excellente réponse ! ")
    else:
        st.write("Mauvaise réponse ! ")

st.subheader("Question 3 : ")
with st.form("question3"):
    reponse3 = st.text_input("Quel artiste français a vendu le plus d'album ? ")
    button = st.form_submit_button("Confirm")
if button:
    if reponse3.lower() == "Johnny Hallyday":
        st.write(" Bonne réponse ! ")
    else:
        st.write("Mauvaise réponse ! ")
