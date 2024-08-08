import streamlit as st
from auth import login_user

def show():
    st.title("Login")
    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        user = login_user(email, password)
        if user:
            st.session_state['user'] = user
            st.rerun()
        else:
            st.error("Invalid email or password")