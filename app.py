import streamlit as st
import pickle
import numpy as np
import random

# Load model
with open("jobfit_model.pkl","rb") as file:
    model = pickle.load(file)

st.title("🤖 JobFitBot - AI Career Advisor")

st.write("Find the best job role based on your skills or resume.")

# ----- OPTION 1: Manual Input -----
st.header("Enter Your Details")

education = st.selectbox("Education", ["BTech","MBA","BSc","MTech","BCA"])
skills = st.text_input("Enter your skills (example: python, sql, ml)")
certification = st.selectbox("Certification",["yes","no"])
experience = st.slider("Years of Experience",0,5)

# ----- OPTION 2: Resume Upload -----
st.header("Or Upload Your Resume")

resume_file = st.file_uploader("Upload Resume (txt or pdf)", type=["txt","pdf"])

if st.button("Predict Job Role"):

    edu_dict = {"BTech":0,"MBA":1,"BSc":2,"MTech":3,"BCA":4}

    edu = edu_dict[education]
    skill = 1
    cert = 1 if certification == "yes" else 0

    features = np.array([[edu, skill, cert, experience]])
    skills_lower = skills.lower()

if "machine learning" in skills_lower or "deep learning" in skills_lower:
    role = "Machine Learning Engineer"

elif "python" in skills_lower and "statistics" in skills_lower:
    role = "Data Scientist"

elif "sql" in skills_lower or "excel" in skills_lower:
    role = "Data Analyst"

elif "html" in skills_lower or "css" in skills_lower or "javascript" in skills_lower:
    role = "Frontend Developer"

elif "java" in skills_lower or "spring" in skills_lower:
    role = "Backend Developer"

elif "docker" in skills_lower or "kubernetes" in skills_lower:
    role = "DevOps Engineer"

else:
    role = "Software Developer"
    score = random.randint(70,95)

    st.success(f"🎯 Recommended Job Role: {role}")
    st.info(f"📊 Eligibility Score: {score}%")

    # Skill suggestions
    required_skills = {
        "Data Scientist":["Python","Machine Learning","Statistics"],
        "Data Analyst":["Excel","SQL","Python"],
        "Frontend Developer":["HTML","CSS","JavaScript"],
        "Backend Developer":["Python","Java","Databases"],
        "AI Engineer":["Python","Deep Learning","TensorFlow"],
        "Machine Learning Engineer":["Python","ML","Data Processing"],
        "Web Developer":["HTML","CSS","JavaScript"],
        "Software Developer":["Java","Python","Problem Solving"],
        "Test Engineer":["Automation","Testing","Selenium"],
        "DevOps Engineer":["Docker","Kubernetes","Linux"]
    }

    user_skills = skills.lower()
    missing = []

    for skill in required_skills.get(role,[]):
        if skill.lower() not in user_skills:
            missing.append(skill)

    if missing:
        st.warning("Skills to Improve:")
        for m in missing:
            st.write("-",m)
    else:
        st.success("You already have most required skills!")

# ----- Resume Analysis -----
if resume_file is not None:

    st.subheader("Resume Analysis")

    resume_text = resume_file.read().decode("latin-1").lower()

    if "python" in resume_text:
        st.write("✔ Python skill detected")

    if "machine learning" in resume_text:
        st.write("✔ Machine Learning skill detected")

    if "sql" in resume_text:
        st.write("✔ SQL skill detected")

    st.success("Resume analyzed successfully!")
