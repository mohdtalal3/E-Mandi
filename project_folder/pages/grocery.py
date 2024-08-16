# grocery.py
import streamlit as st
import sqlite3
import base64
from datetime import datetime
import pandas as pd
import io
from styles import grocery_item_style ,search_bar_style
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS groceries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  type TEXT NOT NULL,
                  season TEXT NOT NULL,
                  picture BLOB)''')
    c.execute('''CREATE TABLE IF NOT EXISTS daily_entries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  grocery_id INTEGER,
                  subtype TEXT,
                  quality TEXT,
                  price REAL,
                  video BLOB,
                  image BLOB,
                  date DATE,
                  type TEXT,
                  FOREIGN KEY (user_id) REFERENCES users(id),
                  FOREIGN KEY (grocery_id) REFERENCES groceries(id))''')
    conn.commit()
    conn.close()

def add_grocery(name, type, season, picture):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO groceries (name, type, season, picture) VALUES (?, ?, ?, ?)",
              (name, type, season, picture))
    conn.commit()
    conn.close()

def get_groceries(type, season=None, search=None):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    query = "SELECT * FROM groceries WHERE type=?"
    params = [type]
    if season:
        query += " AND season=?"
        params.append(season)
    if search:
        query += " AND name LIKE ?"
        params.append(f"%{search}%")
    c.execute(query, params)
    groceries = c.fetchall()
    conn.close()
    return groceries

def add_daily_entry(user_id, grocery_id, subtype, quality, price, video, image, date,type1):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("""INSERT INTO daily_entries 
                 (user_id, grocery_id, subtype, quality, price, video, image, date,type) 
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)""",
              (user_id, grocery_id, subtype, quality, price, video, image, date,type1))
    conn.commit()
    conn.close()

def get_daily_entries(start_date, end_date):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("""SELECT u.name, u.email, u.phone, g.name, d.subtype, d.quality, d.price, d.date
                 FROM daily_entries d
                 JOIN users u ON d.user_id = u.id
                 JOIN groceries g ON d.grocery_id = g.id
                 WHERE d.date BETWEEN ? AND ?""", (start_date, end_date))
    entries = c.fetchall()
    conn.close()
    return entries

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

def show(grocery_type):
    init_db()
    st.title(f"{grocery_type.capitalize()} Groceries")

    # Add the CSS styles
    st.markdown(grocery_item_style, unsafe_allow_html=True)
    st.markdown(search_bar_style, unsafe_allow_html=True)

    # Add new grocery using expander
    add_grocery_expander = st.expander("➕ Add New Grocery", expanded=False)
    with add_grocery_expander:
        with st.form(f"add_grocery_form", clear_on_submit=True, border=True):
            name = st.text_input("Name")
            season = st.selectbox("Season", ["Spring", "Summer", "Autumn", "Winter"])
            picture = st.file_uploader("Upload Picture", type=["jpg", "png", "jpeg"])
            submitted = st.form_submit_button("Add")
            if submitted and name and season and picture:
                picture_bytes = picture.getvalue()
                add_grocery(name, grocery_type, season, picture_bytes)
                st.success("Grocery added successfully!")
                add_grocery_expander.expanded = False
                st.rerun()

    # Filter and search
    col1, col2 = st.columns([3, 1])
    with col1:
        search = st.text_input("Search by name", key="search_input")
    with col2:
        current_season = get_current_season()
        season_filter = st.selectbox("Filter by Season", ["Auto Detect", "All Seasons"], key="season_filter")
        if season_filter == "Auto Detect":
            season_filter = current_season

    # Display groceries
    groceries = get_groceries(grocery_type, season_filter if season_filter != "All Seasons" else None, search)
    
    col1, col2, col3 = st.columns(3)
    for i, grocery in enumerate(groceries):
        with [col1, col2, col3][i % 3]:
            image_b64 = base64.b64encode(grocery[4]).decode()
            st.markdown(f"""
            <div class="grocery-item">
                <img src="data:image/jpeg;base64,{image_b64}" alt="{grocery[1]}">
                <h3>{grocery[1]}</h3>
                <p>Season: {grocery[3]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            daily_entry_expander = st.expander(f"Add Daily Entry for {grocery[1]}", expanded=False)
            with daily_entry_expander:
                with st.form(f"daily_entry_{grocery[0]}", clear_on_submit=True, border=True):
                    subtype = st.text_input("Subtype (e.g., type of grape)")
                    quality = st.selectbox("Quality", ["High", "Low", "Medium"])
                    type = st.selectbox("Type", ["Distributor","Mandi Wala"])
                    price = st.number_input("Price", min_value=0.0, step=0.1)
                    video = st.file_uploader("Upload Video", type=["mp4", "mov"])
                    image = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
                    date = st.date_input("Date")
                    
                    if st.form_submit_button("Submit"):
                        user_id = st.session_state['user'][0]  # Assuming user ID is stored in session state
                        video_bytes = video.read() if video else None
                        image_bytes = image.read() if image else None
                        add_daily_entry(user_id, grocery[0], subtype, quality, price, video_bytes, image_bytes, date,type)
                        st.success("Daily entry added successfully!")
                        daily_entry_expander.expanded = False
                        #st.rerun()  # This will refresh the page, closing the form and allowing for new entries

    if st.button("Back to Dashboard"):
        st.session_state['show_grocery'] = False
        st.rerun()