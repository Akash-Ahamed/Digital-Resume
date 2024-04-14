import streamlit as st
from pathlib import Path
from PIL import Image


# Path Setting............................
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "Profile_pict_nB.jpg"

# Page Contents...........................
PAGE_TITLE = "Digital CV | Akash Ahamed"
PAGE_ICON = ":wave:"


# Personal Content.........................
NAME = "Akash Ahamed"
ADDRESS = "House No:14, Road No: 06, Satmosjid Housing, Chaduddan, Mohammadpur, Dhaka"
CONTACT = "Cell Phone: +880 1796659947"
EMAIL = "Akash.Ahmed.engr@gmail.com"
SOCIAL_MEDIA = {
    "Linkedin": "Akash.ahamed",
    "GitHub": "https://github.com/Akash-Ahamed",
    "Websit" : "www.akash.ahamed",
}

PROJECTS ={
    "Digital Resume - Build a digital resume using python and streamlit": "https://github.com/Akash-Ahamed/Digital-Resume.git",
    "Sample One - Build a digital resume using python and streamlit": "https://github.com/Akash-Ahamed/Digital-Resume.git",
    "Sample Two - Build a digital resume using python and streamlit": "https://github.com/Akash-Ahamed/Digital-Resume.git",
}

# Streamlit connect the Page content........................
st.set_page_config(page_title=PAGE_TITLE,page_icon= PAGE_ICON)


# Load CSS file PDF, Profile picture................
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# Streamlit Codeing.........................................
col1, col2 = st.columns(2, gap="small")
with col1:
    st.title(NAME)
    st.write(ADDRESS)
    st.write(CONTACT)
    st.write(EMAIL)
    st.download_button(
        label="Download Resume",
        data= PDFbyte,
        file_name= resume_file.name,
        mime= "application/octet-stream",
    )
    

with col2:
    st.image(profile_pic, width=230)


# Social Link Display........................................
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index,(platrorm,link) in enumerate (SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platrorm}]({link})")

st.write("_ _ _")
# Skills.......................................................
#st.write("#")
#st.write("_ _ _")
st.header("Skills")
st.write("""
         - Programming Languages: Python, SQL, Dart, C
         - Database: MySQL, Vector Database
         - Machine Learning Technologies:
         - Analytical Tools: Pandas, Numpy,
         - Framework: Streamlit
         - Version Control: Git & GitHub
         - Project Management Tools: Jira
         - Soft Skills:
          """)

# Education....................................................
st.write("#")
st.header("Education")
st.subheader("University of Liberal Arts Bangladesh")
st.write("""
         - Bachelor of Science - Computer Science and Engineering
         - CGPA: 3.51/4.0 
          """)

# Project.......................................................
st.write("_ _ _")
st.header("Projects")
for project, link in PROJECTS.items():
    st.write(f"[{project}] ({link})")