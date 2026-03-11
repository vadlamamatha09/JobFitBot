import streamlit as st
import random

st.title("🤖 JobFitBot - AI Career Advisor")
st.write("Find the best career based on your skills or resume")

# ---------------- EDUCATION ----------------

education = st.selectbox("Education", ["B.Tech","Degree","MBA","M.Tech"])

branches = {
"B.Tech":["Computer Science","Information Technology","Electronics","Mechanical","Civil","AI & ML","Data Science"],
"Degree":["BSc Computer Science","BCom","BBA","BA"],
"MBA":["Finance","Marketing","HR","Business Analytics"],
"M.Tech":["AI","Data Science","Cyber Security","Software Engineering"]
}

branch = st.selectbox("Branch", branches[education])

skills_input = st.text_input("Enter your skills (example: python, sql, machine learning)")
certification = st.selectbox("Certification",["Yes","No"])
experience = st.slider("Years of Experience",0,10)

# ---------------- JOB DATABASE ----------------
job_roles = {

# AI & Data
"Data Scientist":["python","machine learning","statistics","pandas","numpy","data analysis"],
"Machine Learning Engineer":["python","machine learning","deep learning","tensorflow","pytorch"],
"AI Engineer":["python","deep learning","nlp","computer vision"],
"Data Analyst":["excel","sql","power bi","tableau","data analysis"],
"Data Engineer":["python","sql","spark","hadoop","etl"],
"Business Intelligence Analyst":["power bi","tableau","sql","data visualization"],
"Statistician":["statistics","r","data analysis"],

# Software Development
"Software Developer":["java","python","c++","algorithms","data structures"],
"Frontend Developer":["html","css","javascript","react","angular"],
"Backend Developer":["java","python","node","spring","api"],
"Full Stack Developer":["html","css","javascript","node","react","mongodb"],
"Web Developer":["html","css","javascript","php","wordpress"],
"API Developer":["api","python","node","rest"],
"Game Developer":["unity","c#","game development"],

# Mobile
"Mobile App Developer":["android","kotlin","flutter","react native"],
"Android Developer":["android","kotlin","java"],
"IOS Developer":["swift","ios","mobile development"],

# DevOps & Cloud
"DevOps Engineer":["docker","kubernetes","linux","aws","ci/cd"],
"Cloud Engineer":["aws","azure","cloud","terraform","linux"],
"Site Reliability Engineer":["linux","cloud","monitoring","devops"],
"Cloud Architect":["cloud","aws","architecture"],

# Cyber Security
"Cyber Security Analyst":["cyber security","network security","ethical hacking"],
"Penetration Tester":["ethical hacking","penetration testing","security"],
"Security Engineer":["security","network","linux"],
"Security Consultant":["cyber security","risk","security"],

# Blockchain
"Blockchain Developer":["blockchain","solidity","ethereum","web3"],

# Testing
"QA Engineer":["testing","automation","selenium","manual testing"],
"Automation Tester":["selenium","automation testing","python"],

# Design
"UI UX Designer":["figma","ui design","ux design","prototyping"],
"Graphic Designer":["photoshop","illustrator","design"],
"Product Designer":["design","figma","ui","ux"],
"Animator":["animation","blender","3d"],
"Video Editor":["video editing","premiere pro","after effects"],

# Business
"Business Analyst":["excel","sql","business analysis","communication"],
"Product Manager":["product management","strategy","communication"],
"Project Manager":["project management","agile","scrum"],
"Operations Manager":["operations","management","strategy"],

# Marketing
"Digital Marketing Specialist":["seo","social media","google ads"],
"SEO Specialist":["seo","analytics","keyword research"],
"Content Marketing Manager":["content marketing","seo","writing"],
"Social Media Manager":["social media","marketing","branding"],
"Brand Manager":["branding","marketing","strategy"],

# Sales
"Sales Executive":["sales","communication","negotiation"],
"Sales Manager":["sales","leadership","strategy"],
"Business Development Manager":["business development","sales","strategy"],

# Finance
"Financial Analyst":["finance","excel","financial modeling"],
"Accountant":["accounting","finance","tax"],
"Investment Banker":["finance","investment","analysis"],
"Risk Analyst":["risk","finance","analysis"],

# HR
"HR Executive":["recruitment","hr","communication"],
"HR Manager":["hr management","recruitment","leadership"],
"Talent Acquisition Specialist":["recruitment","hiring","communication"],

# Education
"Teacher":["teaching","communication","subject knowledge"],
"Lecturer":["teaching","research","presentation"],
"Professor":["research","teaching","publication"],

# Misc Tech
"Network Engineer":["networking","routers","switches"],
"Database Administrator":["sql","database","oracle"],
"System Administrator":["linux","servers","network"],
"IT Support Specialist":["technical support","network","troubleshooting"]
}

# ---------------- RESUME UPLOAD ----------------

st.header("Upload Resume (Optional)")

resume_file = st.file_uploader("Upload Resume (txt or pdf)", type=["txt","pdf"])

resume_text = ""

if resume_file is not None:
    resume_text = resume_file.read().decode("latin-1").lower()
    st.success("Resume uploaded successfully")

# ---------------- CAREER PREDICTION ----------------
scores = {}

for role, req_skills in job_roles.items():

    match = len(set(user_skills) & set(req_skills))

    score = (match / len(req_skills)) * 100

    scores[role] = score

# Sort roles
sorted_roles = sorted(scores.items(), key=lambda x: x[1], reverse=True)

top_roles = sorted_roles[:3]

st.subheader("🏆 Top Career Recommendations")

for role, score in top_roles:

    score = int(score)

    st.success(f"🎯 {role}")
    st.write(f"Eligibility Score: {score}%")

    if role in salary_data:
        st.write(f"💰 Average Salary: {salary_data[role]}")

    missing = [s for s in job_roles[role] if s not in user_skills]

    if missing:
        st.write("📚 Skills to Improve:")
        for m in missing[:4]:
            st.write("-", m)

    st.write("---")

st.balloons()

