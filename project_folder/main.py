import streamlit as st
from pages import login, signup, dashboard
from database import init_db

def main():
    init_db()
    st.set_page_config(page_title="Agri-App", layout="wide")

    if 'user' not in st.session_state:
        if 'page' not in st.session_state:
            st.session_state['page'] = 'login'

        if st.session_state['page'] == 'login':
            login.show()
        elif st.session_state['page'] == 'signup':
            signup.show()
    else:
        dashboard.show()

if __name__ == "__main__":
    main()