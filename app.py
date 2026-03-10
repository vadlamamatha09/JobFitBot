import streamlit as st

st.title("🤖 JobFitBot - AI Job Role Predictor")
st.write("This application predicts the most suitable job role based on user skills using Machine Learning.")
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
    if st.button("Predict Job Role"):
        job_roles = {
1: "Data Scientist",
2: "Data Analyst",
3: "Frontend Developer",
4: "Backend Developer",
5: "AI Engineer",
6: "Machine Learning Engineer",
7: "Web Developer",
8: "Software Developer",
9: "Test Engineer",
10: "DevOps Engineer"
}

prediction = model.predict([skills])
st.success(f"Recommended Job Role: {job_roles.get(prediction[0], 'Unknown Role')}")
