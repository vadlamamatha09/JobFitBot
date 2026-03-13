import streamlit as st

st.set_page_config(page_title="JobFitBot AI", page_icon="🤖", layout="wide")

# ---------- CUSTOM UI ----------

st.markdown("""
<style>

.main {
background: linear-gradient(to right, #4facfe, #00f2fe);
}

h1 {
color: white;
}

.stButton>button {
background-color:#ff6b6b;
color:white;
border-radius:10px;
font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.markdown(
"<h1 style='text-align:center;'>🤖 JobFitBot – AI Career Advisor</h1>",
unsafe_allow_html=True
)

st.markdown(
"<p style='text-align:center;font-size:18px;'>AI system that predicts the best career and job readiness</p>",
unsafe_allow_html=True
)

st.write("---")

# ---------- MODE ----------

mode = st.radio(
"Choose Mode",
["🚀 Urgent Job Needed","📈 Career Guidance"]
)

# ---------- EDUCATION ----------

education = st.selectbox(
"Education",
["B.Tech","Degree","MBA","M.Tech"]
)

# ---------- SKILLS ----------

skills = st.text_input(
"Enter your skills (example: python, sql, machine learning)"
)

skills_lower = skills.lower()

# ---------- RESUME UPLOAD ----------

resume = st.file_uploader("Upload Resume", type=["txt"])

resume_text = ""

if resume:
    resume_text = str(resume.read())
    st.success("Resume uploaded successfully")

st.write("---")

# ---------- JOB READINESS SCORE ----------

score = 0

if "python" in skills_lower:
    score += 30
if "sql" in skills_lower:
    score += 25
if "machine learning" in skills_lower:
    score += 25
if "project" in skills_lower:
    score += 20

st.subheader("🎯 Job Readiness Score")

st.progress(score/100)

st.write(score,"/100")

st.write("---")

# ---------- URGENT JOB MODE ----------

if mode == "🚀 Urgent Job Needed":

    st.subheader("💼 Immediate Job Matches")

    if "python" in skills_lower:
        st.success("Python Developer")

    elif "sql" in skills_lower:
        st.success("Data Analyst")

    elif "testing" in skills_lower:
        st.success("Software Tester")

    else:
        st.warning("Few job matches found with current skills")

# ---------- CAREER GUIDANCE ----------

else:

    st.subheader("🏆 Top Career Matches")

    roles = []
    scores = []

    if "machine learning" in skills_lower:
        roles.append("ML Engineer")
        scores.append(90)

    if "python" in skills_lower and "statistics" in skills_lower:
        roles.append("Data Scientist")
        scores.append(85)

    if "sql" in skills_lower:
        roles.append("Data Analyst")
        scores.append(80)

    if "html" in skills_lower or "css" in skills_lower:
        roles.append("Web Developer")
        scores.append(75)

    if roles:

        for r,s in zip(roles,scores):
            st.success(f"{r} – {s}% match")

        # ---------- CHART ----------
import pandas as pd
data = {
    "Role": roles,
    "Match %": scores
}
df = pd.DataFrame(data)
st.bar_chart(df.set_index("Role"))
else:
st.warning("No strong career matches detected")

# ---------- SKILL GAP ----------

st.write("---")

st.subheader("⚠ Skill Gap Analysis")

if "python" in skills_lower and "sql" not in skills_lower:
    st.warning("Learning SQL can improve your chances")

if "machine learning" in skills_lower and "statistics" not in skills_lower:
    st.warning("Statistics required for ML roles")

if "html" in skills_lower and "javascript" not in skills_lower:
    st.warning("Learn JavaScript for better web jobs")

# ---------- JOB LINKS ----------

st.write("---")

st.subheader("💼 Apply for Jobs")

st.markdown("Data Analyst Jobs: https://www.naukri.com/data-analyst-jobs")

st.markdown("Python Developer Jobs: https://www.linkedin.com/jobs/")

st.markdown("Software Tester Jobs: https://www.indeed.com/jobs?q=software+tester")

# ---------- CHATBOT ----------

st.write("---")

st.subheader("🤖 Ask CareerBot")

question = st.text_input("Ask a career question")

if question:

    q = question.lower()

    if "data scientist" in q:
        st.write("Skills: Python, Statistics, Machine Learning")

    elif "ai engineer" in q:
        st.write("Skills: Python, Deep Learning, TensorFlow")

    elif "web developer" in q:
        st.write("Skills: HTML, CSS, JavaScript")

    else:
        st.write("Focus on coding skills and building projects")

# ---------- FOOTER ----------

st.write("---")

st.markdown(
"<p style='text-align:center;'>Developed using Streamlit | JobFitBot AI</p>",
unsafe_allow_html=True
)
