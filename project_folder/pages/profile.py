# pages/profile.py
import streamlit as st
import sqlite3

def get_user_details(user_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = c.fetchone()
    conn.close()
    return user

def show():
    st.title("User Profile")
    
    user = get_user_details(st.session_state['user'][0])
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if user[8]:  # Check if user has a profile picture
            st.image(user[8], caption="Profile Picture", use_column_width=True)
        else:
            st.write("No profile picture uploaded")
    
    with col2:
        st.write(f"**Name:** {user[3]}")
        st.write(f"**Email:** {user[1]}")
        st.write(f"**Region:** {user[4]}")
        st.write(f"**District:** {user[5]}")
        st.write(f"**Tehsil:** {user[6]}")
        st.write(f"**Phone:** {user[7]}")
        
    
    if st.button("Back to Dashboard"):
        st.session_state['show_profile'] = False
        st.rerun()