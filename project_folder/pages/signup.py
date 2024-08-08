import streamlit as st
from auth import register_user

def show():
    st.title("Sign Up")
    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    name = st.text_input("Name")
    region = st.text_input("Region")
    district = st.text_input("District")
    tehsil = st.text_input("Tehsil")
    phone = st.text_input("Phone Number")
    picture = st.file_uploader("Upload Picture", type=["jpg", "png", "jpeg"])
    
    if st.button("Sign Up"):
        if picture:
            picture_bytes = picture.read()
        else:
            picture_bytes = None
        
        register_user(email, password, name, region, district, tehsil, phone, picture_bytes)
        st.success("Account created successfully. Please log in.")
        st.rerun()