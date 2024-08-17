import streamlit as st
import sqlite3
from pages import login, signup, dashboard, admin_dashboard1
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
        # Check user type and show appropriate dashboard
        user = st.session_state['user']
        if isinstance(user, tuple):
            user_type = user[-1]  # Assuming user_type is the last element in the tuple
        elif isinstance(user, dict):
            user_type = user.get('user_type')
        else:
            user_type = None

        if user_type == 'Employee':
            dashboard.show()
        elif user_type == 'Admin':
            admin_dashboard1.show()
        else:
            st.error(f"Invalid user type: {user_type}")

if __name__ == "__main__":
    main()

