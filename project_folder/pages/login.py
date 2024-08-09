import streamlit as st
from auth import login_user

def show():
    st.title("Login")
    
    with st.form("login_form", clear_on_submit=True):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        
        submit_button = st.form_submit_button("Login")
        
        if submit_button:
            user = login_user(email, password)
            if user:
                st.session_state['user'] = user
                st.rerun()
            else:
                st.error("Invalid email or password")
    
    st.write("Don't have an account?")
    if st.button("Register"):
        st.session_state['page'] = 'signup'
        st.rerun()