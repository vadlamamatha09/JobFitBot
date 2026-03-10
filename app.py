
import streamlit as st
import pickle

with open("jobfit_model.pkl","rb") as file:
    model=pickle.load(file)

st.title("JobFitBot - Job Eligibility Predictor")

education = st.selectbox("Education", ["BTech","MBA","BSc","MTech","BCA"])
skills = st.text_input("Enter your skills")
certification = st.selectbox("Certification",["yes","no"])
experience = st.slider("Years of Experience",0,5)

if st.button("Predict Job"):

    edu = 1
    skill = 1
    cert = 1 if certification=="yes" else 0

    prediction = model.predict([[edu,skill,cert,experience]])

    st.success("You are eligible for a suitable job role!")
