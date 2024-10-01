import streamlit as st

# Set page title
st.set_page_config(page_title="Manuella Valadares", page_icon="desktop_computer", layout="centered", initial_sidebar_state="auto")

class AboutMe:
    def __init__(self, title, about, img):
        self.title = title
        self.about = about
        self.img = img

    def display(self):
        col1, col2, col3 = st.columns([1.5, 0.1, 1.2])
        with col1:
            st.markdown(f"<h2 style='font-size: 36px;'>{self.title}</h2>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify;'>{self.about}</div>", unsafe_allow_html=True)

            st.markdown("""
                <div style="margin-top: 20px;">
                    <p><a href="https://github.com/manuvaladares" style="text-decoration: none;">💻 Github</a></p>
                    <p><a href="https://www.linkedin.com/in/manuella-valadares-440661232/" style="text-decoration: none;">🔗 LinkedIn</a></p>
                    <p><a href="mailto:manuella.valadares@hotmail.com" style="text-decoration: none;">📨 Email</a></p>
                    <p><a href="http://lattes.cnpq.br/9815810102046557" style="text-decoration: none;">📝 Lattes </a></p>
                </div>
            """, unsafe_allow_html=True)

        with col3:           
            st.image(self.img, use_column_width=True)

# Description
description = """
Undergraduate student in the fifth semester of Software Engineering at the University of Brasília and a research student at the <a href="https://itrac.unb.br/" target="_blank" style="text-decoration: none;">ITRAC</a> Research Laboratory. I have experience and a strong interest in the Data Science field, where I am continuously improving my Python skills. With a particular interest in academic research, I am always seeking new opportunities to contribute to studies and innovations, especially in the fields of data science and Machine Learning.
"""

# Display content
about = AboutMe("Manuella Valadares", description, "img/profile/home_img.svg")
about.display()

st.divider()

# Academic Background Section
st.subheader("Academic Background")
st.write("**Software Engineering** - University of Brasília (2022 - 2027)")
st.write("For information about the curriculum structure, visit the [University of Brasília](https://fga.unb.br/engenharia-de-software/).")
st.divider()

# Professional Experience Section
st.subheader("Professional Experience")
st.write("##### Data Analysis Intern, CAESB (2024)")
st.write("""
- Worked on a predictive panel for the consumption of chemical products at Sewage Treatment Plants (ETEs), aiming to optimize operational efficiency.
- Learned and applied Artificial Intelligence knowledge with Machine Learning models.
""")
st.write("##### Junior Front-End Developer, Baitts (2023-2024)")
st.write("""
- Assisted in the initial creation of the website for the Startup Baitts, a company created by women.
- Learned and applied knowledge in Next.js.
- Contributed to solving user experience-related issues.
""")
st.divider()

# Technical Skills Section
st.subheader("Technical Skills")
st.write("""
- **Programming languages:** Python, Java (OOP), C
- **Libraries and frameworks:** Pandas, Streamlit, Plotly, Selenium
- **Web development:** HTML5, CSS3, JavaScript, Next.js
- **Version control:** Git
- **Agile methodologies:** Scrum
- **Formatting tools:** LaTeX
""")
st.divider()

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: grey;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>Developed by Manuella Valadares &copy; 2024</p>
    </div>
    """,
    unsafe_allow_html=True
)
