import streamlit as st
from helper import styles
from pathlib import Path
from PIL import Image


st.set_page_config(
    page_title="Digital CV | Andrews Boateng",
    page_icon="🧾",
    initial_sidebar_state="collapsed",
    layout="centered",
)

styles.load_css_file("styles/main.css")


st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True,
)

st.markdown(
    """
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #002b36;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/aaboateng" target="_blank">Andrews Asamoah Boateng</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#summary">Summary<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
    <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="#publications">Publications</a>
    </li>
      <li class="nav-item">
        <a class="nav-link" href="#licenses">Licenses</a>
      </li>
    </ul>
  </div>
</nav>
""",
    unsafe_allow_html=True,
)


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "Andrews Asamoah Boateng Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jfif"


# --- GENERAL SETTINGS ---
NAME = "Andrews Boateng"
DESCRIPTION = """
Developer/Analyst assisting organizations to 10x profitability via data-driven insights and tools.
"""
EMAIL = "andrewsboateng137@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/aaboateng",
    "GitHub": "https://github.com/drekwasi",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


def little_headers(a, b):
    (
        col1,
        col2,
    ) = st.columns([2, 1])
    with col1:
        st.write(a)
    with col2:
        st.write(b)


def content_txt(a, b):
    (
        col1,
        col2,
    ) = st.columns([1, 2])
    with col1:
        st.write(a)
    with col2:
        st.write(b)


st.subheader("Summary")
st.write(
    """Self-motivated data analyst and Python developer with over 3 years of experience in data analytics and Python
development. Implemented cost-saving solutions, including a medication alternatives suggestion app and an order
review model, resulting in over $400K in savings. Proficient in Python, SQL, and Excel with experience in
microservice development and data analytics. Seeks to optimize efficiency for healthcare organizations
using analytics-based demand planning and business intelligence"""
)
st.markdown("----")


st.subheader("Education")
little_headers("**Bachelor of Pharmacy**, University of Ghana (Legon)", "2015-2019")
st.markdown("----")

st.subheader("Work Experience")
little_headers("**Customer Solutions** | mPharma", "April, 2021 to Present")
st.markdown(
    """
- 🚙 Implemented a supply chain tool using Streamlit to automate alternative medication suggestions,
resulting in over $400K in cost-savings from reduced expiry risks in the first 12 months.
- 🚙 Created an Order Review Model using Streamlit, Python, and Metabase to streamline monthly
orders for proprietary facilities, resulting in $30K in cost-savings in just one month.
- 🚙 Improved response times of key revenue drivers by 50% through the creation of dashboards using
Google Sheets, AppScript, and Excel to track revenue growth KPIs.
- 🚙 Boosted efficiency in data acquisition by developing a mock-up ETL process to automate
a set of data quality checks resulting in a 65% decrease in data processing time.
"""
)

little_headers(
    "**Research Associate (Data Scientist)** | West African Centre for Cell Biology of Infectious Pathogens (WACCBIP)",
    "Jun 2020 to Nov 2021",
)
st.markdown(
    """
- 🥼 Successfully implemented a Principal Component Analysis to improve the cross-discrimination between
biomarkers, resulting in a 50% improvement in feature selection efficiency
- 🥼 Developed a feature selection algorithm based on Cluster Resolution Feature Selection using python,
which identified approximately 10 putative biomarkers from a pool of more than 60 features/biomarkers
    """
)

little_headers(
    "**Volunteer Research Associate** | University of Ghana (School of Pharmacy)",
    "Dec, 2019 to Present",
)
st.markdown(
    """
- 👨‍🏫 Built an ML Classification Model to identify between origins of honey and differentiate pure/adulterated
honey products on the Ghanaian market.
- 👨‍🏫 Assisted in training more than 4 project students on employing data science in chemometrics.
    """
)

st.markdown("----")


st.subheader("Skills")
content_txt("🧠Programming Languages", "**`Python`**, **`AppScript`**, **`HTML`** ")
content_txt("📚Frameworks", "`Django`, `Django REST Framework`, `jQuery`, `AJAX`")
content_txt("💫Data processing/wrangling", "`numpy`, `pandas`, `sql`, `vaex`")
content_txt("🎰Machine Learning", "`scikit-learn`")
content_txt("📊Data Visualization", " `ploty`, `matplotlib`, `seaborn`, `Google Sheets`,`Metabase`")
content_txt("🐱‍💻Databases", "`PostgreSQL`")
content_txt("🛩️Model Deployment", "`Streamlit`")
content_txt("🌩️Cloud & Version Control", "`Docker`, `Heroku`, `render`, `Deta`, `Github`")
content_txt("📇Methodologies", "`Functional Programming`, `Object-Oriented Programming`")
st.markdown("----")

st.subheader("Projects")
little_headers("QuickHire | Project Link", "Dec, 2022 - Present")
st.markdown("""Collaborated with Joel Anaman to develop a streamlit web app using the Google’s Custom Search
API to scour job boards via custom search keys""")

little_headers("CSGH | Project Link", "Nov, 2022 – Present")
st.markdown("An All-in-one order processing and inventory web application built with Streamlit")

little_headers("Order Review Model | Project Link", "Oct, 2022 – Present")
st.markdown("Web Application in Streamlit for Order Validation, Insight Analysis and Flow casting.")
st.markdown("----")

st.subheader("Publications")
st.markdown("""Evaluation of chemometric classification and regression models for the detection of syrup
adulteration in honey – Jun, 2022""")
st.markdown("----")

st.subheader("Licenses")
st.markdown("""Pharmacist - Pharmaceutical Society of Ghana (License Number: PSGH 5535)""")
st.markdown("----")
