import streamlit as st
import pickle
import numpy as np

# Load model
with open("jobfit_model.pkl","rb") as file:
    model = pickle.load(file)

st.title("🤖 JobFitBot - AI Job Role Predictor")
st.write("Predict the most suitable job role based on your qualifications.")

# User Inputs
education = st.selectbox("Education", ["BTech","MBA","BSc","MTech","BCA"])
skills = st.text_input("Enter your skills (example: python, ml)")
certification = st.selectbox("Certification",["yes","no"])
experience = st.slider("Years of Experience",0,5)

# Predict Button
if st.button("Predict Job Role"):

    # Encoding inputs
    edu_dict = {"BTech":0,"MBA":1,"BSc":2,"MTech":3,"BCA":4}
    
    edu = edu_dict[education]
    skill = 1
    cert = 1 if certification == "yes" else 0

    features = np.array([[edu, skill, cert, experience]])

    prediction = model.predict(features)

    job_roles = {
        0: "Data Scientist",
        1: "Data Analyst",
        2: "Frontend Developer",
        3: "Backend Developer",
        4: "AI Engineer",
        5: "Machine Learning Engineer",
        6: "Web Developer",
        7: "Software Developer",
        8: "Test Engineer",
        9: "DevOps Engineer"
    }

    predicted_value = int(prediction[0])

    st.success("Recommended Job Role:")
    st.write(job_roles.get(predicted_value,"Software Developer"))
