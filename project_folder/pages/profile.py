import streamlit as st
import sqlite3
import base64

grocery_item_style = """
<style>
    .grocery-item {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 30px;
        margin: 20px auto;
        text-align: center;
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        cursor: pointer;
        max-width: 400px;
        width: 100%;
    }
    .grocery-item:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .grocery-item img {
        width: 200px;
        height: 200px;
        object-fit: cover;
        border-radius: 50%;
        margin-bottom: 20px;
    }
    .grocery-item h3 {
        margin: 10px 0;
        color: #333;
        font-size: 24px;
    }
    .grocery-item p {
        margin: 10px 0;
        color: #666;
        font-size: 16px;
    }
</style>
"""

def get_user_details(user_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = c.fetchone()
    conn.close()
    return user

def show():
    st.title("User Profile")
    
    # Apply the CSS
    st.markdown(grocery_item_style, unsafe_allow_html=True)
    
    user = get_user_details(st.session_state['user'][0])
    
    # Create three columns to center the profile box
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if user[8]:  # Check if user has a profile picture
            image_b64 = base64.b64encode(user[8]).decode()
            st.markdown(f"""
            <div class="grocery-item">
                <img src="data:image/jpeg;base64,{image_b64}" alt="Profile Picture">
                <h3>{user[3]}</h3>
                <p><strong>Email:</strong> {user[1]}</p>
                <p><strong>Region:</strong> {user[4]}</p>
                <p><strong>District:</strong> {user[5]}</p>
                <p><strong>Tehsil:</strong> {user[6]}</p>
                <p><strong>Phone:</strong> {user[7]}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="grocery-item">
                <p>No profile picture uploaded</p>
            </div>
            """, unsafe_allow_html=True)
    
    if st.button("Back to Dashboard"):
        st.session_state['show_profile'] = False
        st.rerun()

if __name__ == "__main__":
    show()