import streamlit as st
from auth import register_user

def show():
    st.title("Sign Up")
    
    with st.form("signup_form", clear_on_submit=True, border=True):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        name = st.text_input("Name")
        region = st.text_input("Region")
        district = st.text_input("District")
        tehsil = st.text_input("Tehsil")
        phone = st.text_input("Phone Number")
        picture = st.file_uploader("Upload Picture", type=["jpg", "png", "jpeg"])
        user_type = st.selectbox("User Type", ["Employee", "Admin"])
        
        submit_button = st.form_submit_button("Sign Up")
        
        if submit_button:
            if picture:
                picture_bytes = picture.read()
            else:
                picture_bytes = None
            
            register_user(email, password, name, region, district, tehsil, phone, picture_bytes, user_type)
            st.success("Account created successfully. Please log in.")
            st.session_state['page'] = 'login'
            st.rerun()

    st.write("Already have an account?")
    if st.button("Login"):
        st.session_state['page'] = 'login'
        st.rerun()