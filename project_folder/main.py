import streamlit as st
from pages import login, signup, dashboard
from database import init_db

def main():
    init_db()
    st.set_page_config(page_title="Agri-App", layout="wide")

    if 'user' not in st.session_state:
        st.sidebar.title("Welcome")
        page = st.sidebar.selectbox("Choose an option", ["Login", "Sign Up"])

        if page == "Login":
            login.show()
        elif page == "Sign Up":
            signup.show()
    else:
        dashboard.show()

if __name__ == "__main__":
    main()