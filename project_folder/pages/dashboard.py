# pages/dashboard.py
import streamlit as st
from datetime import datetime
from pages import profile, grocery

def get_current_season():
    month = datetime.now().month
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Autumn"
    else:
        return "Winter"

def show():
    st.title("Dashboard")
    
    col1, col2, col3 = st.columns([1,6,1])
    with col3:
        if st.button("👤"):
            st.session_state['show_profile'] = True
            st.rerun()
    
    if 'show_profile' in st.session_state and st.session_state['show_profile']:
        profile.show()
    elif 'show_grocery' in st.session_state and st.session_state['show_grocery']:
        grocery.show(st.session_state['grocery_type'])
    else:
        st.write(f"Welcome, {st.session_state['user'][3]}!")
        
        st.subheader(f"Current Season in Pakistan: {get_current_season()}")
        
        # CSS for the fruit and vegetable buttons
        st.markdown("""
        <style>
            div[data-testid="column"]:nth-of-type(1) .stButton > button {
                background-color: #ffcccb;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                cursor: pointer;
                transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
                height: 150px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 24px;
                font-weight: bold;
                color: #333;
                border: none;
                width: 100%;
            }
            div[data-testid="column"]:nth-of-type(2) .stButton > button {
                background-color: #90ee90;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                cursor: pointer;
                transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
                height: 150px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 24px;
                font-weight: bold;
                color: #333;
                border: none;
                width: 100%;
            }
            div[data-testid="column"] .stButton > button:hover {
                transform: scale(1.05);
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }
        </style>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Fruits", key="fruits_button", use_container_width=True):
                st.session_state['show_grocery'] = True
                st.session_state['grocery_type'] = 'fruit'
                st.rerun()
        
        with col2:
            if st.button("Vegetables", key="vegetables_button", use_container_width=True):
                st.session_state['show_grocery'] = True
                st.session_state['grocery_type'] = 'vegetable'
                st.rerun()
    
    if st.sidebar.button("Logout"):
        del st.session_state['user']
        if 'show_profile' in st.session_state:
            del st.session_state['show_profile']
        if 'show_grocery' in st.session_state:
            del st.session_state['show_grocery']
        st.rerun()