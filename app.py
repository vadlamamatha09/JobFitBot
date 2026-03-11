import streamlit as st
import random

st.title("🤖 JobFitBot - AI Career Advisor")
st.write("Find the best career based on your skills and profile")

# ---------------- EDUCATION ----------------

education = st.selectbox("Education", ["B.Tech","Degree","MBA","M.Tech"])

branches = {
"B.Tech":["Computer Science","Information Technology","Electronics","Mechanical","Civil","AI & ML","Data Science"],
"Degree":["BSc Computer Science","BCom","BBA","BA"],
"MBA":["Finance","Marketing","HR","Business Analytics"],
"M.Tech":["AI","Data Science","Cyber Security","Software Engineering"]
}

branch = st.selectbox("Branch",branches[education])

skills = st.text_input("Enter your skills (example: python, sql, machine learning)")
certification = st.selectbox("Certification",["Yes","No"])
experience = st.slider("Years of Experience",0,10)

# ---------------- JOB DATABASE ----------------

job_roles = {

"Data Scientist":["python","machine learning","statistics","pandas","numpy"],
"Machine Learning Engineer":["python","ml","deep learning","tensorflow","pytorch"],
"AI Engineer":["python","nlp","deep learning","computer vision"],
"Data Analyst":["excel","sql","power bi","tableau","data analysis"],
"Business Analyst":["excel","sql","business analysis","communication"],

"Frontend Developer":["html","css","javascript","react","angular"],
"Backend Developer":["java","python","node","spring","databases"],
"Full Stack Developer":["html","css","javascript","node","react","mongodb"],
"Software Developer":["java","python","c++","algorithms"],
"Web Developer":["html","css","javascript","php"],

"DevOps Engineer":["docker","kubernetes","linux","aws","ci/cd"],
"Cloud Engineer":["aws","azure","cloud","terraform"],
"Site Reliability Engineer":["linux","cloud","monitoring","devops"],

"Cyber Security Analyst":["cyber security","network security","ethical hacking"],
"Penetration Tester":["ethical hacking","penetration testing","security"],
"Security Engineer":["cyber security","network security","python"],

"Mobile App Developer":["android","kotlin","flutter","react native"],
"Game Developer":["unity","c#","game development"],

"Blockchain Developer":["blockchain","solidity","ethereum"],
"AR/VR Developer":["unity","vr","ar"],

"UI UX Designer":["figma","ui design","ux design","prototyping"],
"Product Manager":["product management","analytics","communication"],

"Database Administrator":["sql","oracle","database","mysql"],
"System Administrator":["linux","networking","servers"],

"Network Engineer":["networking","ccna","routers"],
"Embedded Engineer":["embedded systems","c","microcontrollers"]

}

# Salary estimation (India)

salary_data = {
"Data Scientist":"₹10L - ₹25L",
"Machine Learning Engineer":"₹12L - ₹30L",
"AI Engineer":"₹12L - ₹28L",
"Data Analyst":"₹5L - ₹12L",
"Business Analyst":"₹6L - ₹14L",
"Frontend Developer":"₹5L - ₹15L",
"Backend Developer":"₹6L - ₹18L",
"Full Stack Developer":"₹7L - ₹20L",
"Software Developer":"₹6L - ₹16L",
"Web Developer":"₹4L - ₹10L",
"DevOps Engineer":"₹10L - ₹25L",
"Cloud Engineer":"₹12L - ₹28L",
"Cyber Security Analyst":"₹8L - ₹22L",
"Mobile App Developer":"₹6L - ₹18L",
"Game Developer":"₹5L - ₹12L",
"Blockchain Developer":"₹15L - ₹40L",
"UI UX Designer":"₹6L - ₹15L"
}

# ---------------- PREDICTION ----------------

if st.button("Predict Career"):

    user_skills = [s.strip().lower() for s in skills.split(",")]

    scores = {}

    for role,req_skills in job_roles.items():

        match = len(set(user_skills) & set(req_skills))
        score = (match/len(req_skills))*100

        scores[role] = score

    top_roles = sorted(scores,key=scores.get,reverse=True)[:3]

    st.subheader("🏆 Top Career Recommendations")

    for role in top_roles:

        score = int(scores[role]) + random.randint(5,15)
        if score>95:
            score=95

        st.success(f"🎯 {role}")
        st.write(f"Eligibility Score: {score}%")

        if role in salary_data:
            st.write(f"💰 Average Salary: {salary_data[role]}")

        missing = [s for s in job_roles[role] if s not in user_skills]

        if missing:
            st.write("📚 Skills to Improve:")
            for m in missing[:4]:
                st.write("-",m)

        st.write("-----")

# ---------------- RESUME ANALYSIS ----------------

st.header("Upload Resume")

resume_file = st.file_uploader("Upload Resume (txt or pdf)",type=["txt","pdf"])

if resume_file:

    text = resume_file.read().decode("latin-1").lower()

    detected = []

    all_skills=set()

    for skills_list in job_roles.values():
        all_skills.update(skills_list)

    for skill in all_skills:
        if skill in text:
            detected.append(skill)

    st.subheader("Detected Skills")

    if detected:
        for s in detected:
            st.write("✔",s)
    else:
        st.write("No skills detected")

    st.success("Resume analyzed successfully")
