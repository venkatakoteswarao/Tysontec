import streamlit as st

# Define pages as functions
def home_page():
    st.title("Home Page")
    st.write("Welcome to the website!")
    st.image("https://via.placeholder.com/800x300", caption="Homepage Banner")

def about_page():
    st.title("About Us")
    st.write("This is the About page of our website.")
    st.markdown("""
    - **Mission**: To build great apps.
    - **Vision**: Empower developers.
    """)

def services_page():
    st.title("Our Services")
    st.write("Explore the services we offer:")
    st.markdown("""
    - Web Development
    - Data Analysis
    - AI/ML Model Development
    """)

def contact_page():
    st.title("Contact Us")
    st.write("Get in touch using the form below:")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success(f"Thank you, {name}! We have received your message.")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "About", "Services", "Contact"])

# Implementing the Search Bar in Sidebar
search_query = st.sidebar.text_input("Search", placeholder="Type to search...")
if search_query:
    st.sidebar.write(f"You searched for: {search_query}")

# Page Routing
if page == "Home":
    home_page()
elif page == "About":
    about_page()
elif page == "Services":
    services_page()
elif page == "Contact":
    contact_page()

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Streamlit Website | © 2024")
