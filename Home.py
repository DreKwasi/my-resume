import streamlit as st
from helper import styles
from pathlib import Path
from PIL import Image
from streamlit_extras.badges import badge



st.set_page_config(
    page_title="Digital CV | Andrews Boateng",
    page_icon="🧾",
    initial_sidebar_state="expanded",
    layout="centered",
)

styles.load_css_file("styles/main.css")

# option_menu(
#     None,
#     ["Resume", "Portfolio"],
#     orientation="horizontal",
#     styles={
#         "container": {"padding": "0!important", "background-color": "#002b36"},
#         "icon": {"color": "white", "font-size": "20px"},
#         "nav-link": {
#             "font-size": "20px",
#             "text-align": "center",
#             "margin": "0px",
#             "--hover-color": "#577678",
#         },
#         "nav-link-selected": {"background-color": "#001e25"},
#     },
# )

st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True,
)

st.markdown(
    """
<nav class="navbar fixed-top navbar-expand-sm navbar-dark" style="background-color: #001E25;">
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
        <a class="nav-link" href="#skills">Skills</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="#volunteer-work-experience">Volunteer Work Experience</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="#publications">Publications & Licenses</a>
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
profile_pic = current_dir / "assets" / "Profile.jpg"


# --- GENERAL SETTINGS ---
NAME = "Andrews Boateng"
DESCRIPTION = """
Backend Developer/Data Analyst assisting organizations to 10x profitability via data-driven tools and insights.
"""
EMAIL = "andrewsboateng137@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/aaboateng",
    "github": "drekwasi",
}

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
# with col1:
#     st.image(profile_pic, width=230)


col1, col2 = st.columns(2, gap="small")

with col1:
    st.title(NAME)

with col2:
    st.markdown("#####")
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

col1, col2, col3 = st.columns(3, gap="small")


st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    if platform == "github":
        with cols[index]:
            badge("github", link)
    else:
        cols[index].write(f"[{platform}]({link})")

st.write(DESCRIPTION)




def little_headers(a, b):
    (
        col1,
        col2,
    ) = st.columns([2, 1], gap="small")
    with col1:
        st.write(a)
    with col2:
        st.write(b)


def content_txt(a, b):
    (
        col1,
        col2,
    ) = st.columns([1, 2], gap="small")
    with col1:
        st.write(a)
    with col2:
        st.write(b)


st.subheader("Summary 🌌")
st.write(
    """As a self-motivated data analyst and Python developer with over 3 years of experience, 
    I specialize in implementing data-driven solutions for organizations which has resulted 
    in over $500K in cost-savings and hundreds of saved man-hours. Proficient in Python, SQL,
    and Spreadsheets, I am dedicated to optimizing efficiency for organizations and increasing 
    profitability via data-driven in-house tools. I strive to leverage my skills and experience
    to identify insights and trends in complex data sets, and effectively communicate findings
    to drive informed business decisions """
)
st.markdown("----")

st.subheader("Skills 🧰")
content_txt("🧠Programming Languages:", "Python, AppScript, HTML ")
content_txt("🧠BI Tools:", "Power BI, Metabase, Streamlit")
content_txt("📚Frameworks:", "Django, Django REST Framework, jQuery, AJAX")
content_txt("💫Data processing/wrangling:", "numpy, pandas, sql, vaex")
content_txt("🎰Machine Learning:", "scikit-learn")
content_txt(
    "📊Data Visualization:", "ploty, matplotlib, seaborn, spreadsheets, Metabase"
)
content_txt("🐱‍💻Databases", "PostgreSQL")
content_txt("🛩️Model Deployment", "Streamlit")
content_txt("🌩️Cloud & Version Control", "Docker, Heroku, render, Deta, Github, Streamlit")
content_txt("📇Methodologies", "Functional & Object-Oriented Programming, REST")
st.markdown("----")

st.subheader("Work Experience 🧑‍💼")
little_headers(
    "**Supply Chain Customer Solutions Associate** | mPharma", "April, 2021 to Present"
)
st.markdown(
    """
- 🚙 Saved **>$400K** in expiry risks by developing an automated
alternative medication suggestions' tool, using data wrangling and deployed with Streamlit.
- 🚙 Collaborated closely with operations and product teams in launching an Order Review Model for 
proprietary facilities utilizing Streamlit and Metabase resulting in cost-savings worth $30K in one month.
- 🚙 Built a data pipeline using BigQuery, implementing data quality improvements with Python 
and reducing data errors by **50%**, leading to a more reliable and accessible data system.
- 🚙 Created data connectors with custom SQL queries from BigQuery to Looker Studio and 
Google Sheets, improving data usability by **85%** and increasing data visibility,
resulting in better-informed business decisions.
- 🚙 Developed Streamlit, Google Sheets, AppScript, and Excel dashboards,
enhancing visibility of key revenue drivers by **60%** for CRM and Order Processing data
- 🚙 Implemented a mock-up ETL process to automate data quality checks, resulting in 
a **65%** decrease in data processing time and improving the overall efficiency of data management.
"""
)

little_headers(
    "**Research Associate (Data Scientist)** | West African Centre for Cell Biology of Infectious Pathogens (WACCBIP)",
    "Jun 2020 to Nov 2021",
)
st.markdown(
    """
- 🥼 Implemented a Principal Component Analysis resulting in a **50%** improvement in feature selection efficiency.
- 🥼 Developed a feature selection algorithm based on Cluster Resolution Feature Selection using python,
identifying approximately 10 putative biomarkers from a pool of >60 biomarkers.
    """
)
st.markdown("----")

st.subheader("Work Experience (Volunteer) 👷‍♂️")

little_headers(
    "**Data/Operations Analyst** | Synlab Ghana", "Jan, 2023 to Present"
)
st.markdown(
    """
- 🧪 Developed a web-based requisition application using Streamlit, Deta,
Google Sheets, and Google Cloud, which resulted in a **70%** 
improvement in internal requisitions processing.
- 🧪 Created a cloud-based dashboard using Streamlit,
Deta, and Google Cloud that enhanced operational visibility by **35%** for business leads and c-suite executives.
- 🧪 Designed a forecasting model by utilizing moving averages and Pareto analysis,
resulting in a **70%** improvement in projected revenue targets for 2023 
while identifying key revenue drivers for the business.
- 🧪 Developed No-SQL queries for fetching and parsing data from low cost cloud platform (Deta) 
reducing expenses in data infrastructure and technologies.
    """
)

little_headers(
    "**Research Associate** | University of Ghana (School of Pharmacy)",
    "Dec, 2019 to Present",
)
st.markdown(
    """
- 👨‍🏫 Built an ML Classification Model with a **>95%** accuracy in differentiating between and origins of honey 
and indentifying the pure/adulterated honey products on the Ghanaian market.
- 👨‍🏫 Trained more than 4 university undergraduates on employing data science in chemometrics.
    """
)

st.subheader("Education 🎒")
little_headers("**Bachelor of Pharmacy**, University of Ghana (Legon)", "2015 to 2019")
st.markdown("----")

st.subheader("Projects 🏗️")
little_headers("[QuickHire](https://quickhire.streamlit.app)", "Dec, 2022 to Present")
st.markdown(
    """Collaborated with Joel Anaman to develop a streamlit web app using the Google's Custom Search
API to scour job boards via custom search keys"""
)

little_headers("[Brazilian E-commerce Analysis](https://olist-ecom.streamlit.app)", "Mar, 2023 to Present")
st.markdown(
    """A Streamlit dashboard built for Ecommerce, Distribution, Customer and Forecasting Analytics."""
)

little_headers(
    "[Order Review Model](https://csghreview.streamlit.app)", "Oct, 2022 to Present"
)
st.markdown(
    "Web Application in Streamlit for Order Validation, Insight Analysis and Flow casting."
)
st.markdown("----")

st.subheader("Publications 📝")
st.markdown(
    """[Evaluation of chemometric classification and regression models for the detection of syrup
adulteration in honey](https://www.sciencedirect.com/science/article/pii/S0023643822004339) - Jun, 2022"""
)
st.markdown("----")

st.subheader("Licenses 🏆")
st.markdown(
    """Pharmacist - Pharmaceutical Society of Ghana (License Number: PSGH 5535)"""
)
st.markdown("----")
