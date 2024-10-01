import streamlit as st

# Page configuration
st.set_page_config(page_title="Manuella Valadares", page_icon="desktop_computer", layout="wide")
st.image("img/gallery/gallery.svg", width=320)

# Page title
##st.header("My Gallery")
st.write("Here are some special moments from my participation in events and talks :)")

# List of events with images
events = [
    {"name": "4th Female Programming Competition at UnB", 
     "description": "I was part of the organizing team of the 4th Female Programming Competition at UnB, organized by Meninas.comp.",
     "image": "img/gallery/3competicao.jpg"},

    {"name": "From Women to Women: Learn with Baitts how to create solutions for women in Technology, on the PyLadies stage at CPBSB6!", 
     "description": "I had the opportunity to participate in the talk 'From Women to Women: Learn with Baitts how to create solutions for women in Technology' on the PyLadies stage at CPBSB6! It was very special to discuss such an important topic alongside BAITTS. An experience I want to live many more times!",
     "image": "img/gallery/campus_party.jpg"},

    {"name": "Girls and Women in Science Exhibition - 03/24", 
     "description": "It was very special to participate in this incredible day! I’m very grateful for the many opportunities that the Meninas.comp Project has provided me. The Girls and Women in Science Exhibition at SESI LAB was amazing 🩷",
     "image": "img/gallery/sesi.jpg"},

    {"name": "SemUni 2024", 
     "description": "On September 26th, I dedicated my day to assisting girls from public schools in the Federal District and surrounding areas to showcase their robotics and software projects at the University of Brasília!",
     "image": "img/gallery/madrinha.jpg"}
]

# Displaying the event gallery in three columns
cols = st.columns(3)
for i, event in enumerate(events):
    with cols[i % 3]:
        st.image(event["image"], use_column_width=True)
        st.markdown(f"**{event['name']}**")
        st.caption(event["description"])

# To avoid unbalanced elements in columns if the number of events is not a multiple of three
if len(events) % 3:
    st.empty()

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