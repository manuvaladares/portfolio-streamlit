import streamlit as st

# Initial page settings
st.set_page_config(page_title="Manuella Valadares", page_icon="desktop_computer", layout="centered", initial_sidebar_state="auto")

# List of projects
projects = [
    {"name": "Meninas.comp",
     "description": "An extension project from the University of Brasília (UnB) that aims to encourage female participation in the field of Computer Science. The project consists of a series of workshops and lectures covering various topics, such as programming, robotics, and artificial intelligence.",
     "link": "https://www.instagram.com/meninas.comp/",
     "image": "img/projects/meninas.comp.png"},
    {"name": "Minas de Cultura", 
     "description": "This is a website developed as part of the Software Development Methods (MDS) course at the University of Brasília (UnB). The main goal of this project is to create an online platform for the analysis and storage of procurement data related to cultural spending supported by the Federal Government, using information from the State of Minas Gerais' Culture Secretariat.", 
     "link": "https://2024-1-minas-de-cultura.vercel.app/", 
     "image": "img/projects/logo_vermelha.png"}
]

# Function to display projects
def display_project(project):
    with st.container():
        # Split into two columns
        col1, col2 = st.columns([1.5, 3])
        
        # Image column
        with col1:
            if project["image"]:
                st.image(project["image"], width=200)  
        
        # Project details column
        with col2:
            # Style to remove link decoration
            st.markdown(f"""
                <h3><a href="{project['link']}" style="text-decoration:none; color:rgb(49, 51, 63);">{project['name']}</a></h3>
            """, unsafe_allow_html=True)
            st.write(project["description"])

# Displaying projects on the page
st.image("img/projects/projects.svg", width=250)
st.write("Here are some university projects I participate in!")

# Display each project from the list
for project in projects:
    display_project(project)
    st.markdown("---")  # Divider line between projects

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