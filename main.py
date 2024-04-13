import streamlit as st
from pathlib import Path
from PIL import Image


# Path Setting............................
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "Profile_pict.jpg"

# Page Contents...........................
PAGE_TITLE = "Digital CV | Akash Ahamed"
PAGE_ICON = ":wave:"


# Personal Content.........................
NAME = "Akash Ahamed"
DESCRIPTION = " AI Engineer"
EMAIL = "Akash.Ahmed.engr@gmail.com"
SOCIAL_MEDIA = {
    "Linkedin": "Akash.ahamed",
    "GitHub": "Akash_Ahamed",
    "Websit" : "www.akash.ahamed",
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
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data= PDFbyte,
        file_name= resume_file.name,
        mime= "application/octet-stream",
    )
    st.write(EMAIL)

with col2:
    st.image(profile_pic, width=230)
