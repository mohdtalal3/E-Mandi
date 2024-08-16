import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
from datetime import datetime, timedelta

def admin_dashboard():
    st.title("Admin Dashboard")

    # Initialize session state
    if 'data' not in st.session_state:
        st.session_state.data = None

    # Date range selection
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime.now() - timedelta(days=30))
    with col2:
        end_date = st.date_input("End Date", datetime.now())

    # Grocery selection
    groceries = get_all_groceries()
    selected_grocery = st.selectbox("Select Grocery", ["All"] + [g[1] for g in groceries])

    if st.button("Fetch Data"):
        data = fetch_data(start_date, end_date, selected_grocery)
        if data:
            df = pd.DataFrame(data, columns=[
                "Employee Name", "Email", "Phone", "Grocery Name", "Type", "Season",
                "Subtype", "Quality", "Price", "Date", "Seller Type", "Region"
            ])
            st.session_state.data = df
            st.dataframe(df)

            # Download button
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"data_{start_date}_{end_date}.csv",
                mime="text/csv",
            )
        else:
            st.warning("No data found for the selected criteria.")
            st.session_state.data = None

    # Graph selection and display
    if st.session_state.data is not None:
        graph_options = [
            "Price Trends Over Time",
            "Grocery Distribution",
            "Quality Distribution",
            "Seller Type Distribution",
            "Regional Price Comparison",
            "Seasonal Price Variations",
            "Daily Entry Count",
            "Top Contributors"
        ]
        selected_graph = st.selectbox("Select a graph to display", graph_options)
        display_graph(st.session_state.data, selected_graph)

def get_all_groceries():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT id, name FROM groceries")
    groceries = c.fetchall()
    conn.close()
    return groceries

def fetch_data(start_date, end_date, selected_grocery):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    query = """
    SELECT u.name, u.email, u.phone, g.name, g.type, g.season,
           d.subtype, d.quality, d.price, d.date, d.type, u.region
    FROM daily_entries d
    JOIN users u ON d.user_id = u.id
    JOIN groceries g ON d.grocery_id = g.id
    WHERE d.date BETWEEN ? AND ?
    """
    
    params = [start_date, end_date]
    
    if selected_grocery != "All":
        query += " AND g.name = ?"
        params.append(selected_grocery)
    
    c.execute(query, params)
    data = c.fetchall()
    conn.close()
    return data

def display_graph(df, selected_graph):
    st.subheader(selected_graph)

    if selected_graph == "Price Trends Over Time":
        fig = px.line(df, x='Date', y='Price', color='Grocery Name', title='Price Trends Over Time')
        st.plotly_chart(fig)
        st.write("This graph shows how the prices of different groceries have changed over time. It can help identify price fluctuations and seasonal trends.")

    elif selected_graph == "Grocery Distribution":
        fig = px.pie(df, names='Grocery Name', title='Distribution of Groceries')
        st.plotly_chart(fig)
        st.write("This pie chart illustrates the distribution of different groceries in the dataset. It helps visualize which groceries are being reported most frequently.")

    elif selected_graph == "Quality Distribution":
        quality_dist = df.groupby(['Grocery Name', 'Quality']).size().unstack(fill_value=0)
        fig = px.bar(quality_dist, title='Quality Distribution by Grocery', barmode='stack')
        st.plotly_chart(fig)
        st.write("This stacked bar chart shows the distribution of quality levels for each grocery type. It can help identify which groceries tend to have higher or lower quality ratings.")

    elif selected_graph == "Seller Type Distribution":
        fig = px.pie(df, names='Seller Type', title='Distribution of Seller Types')
        st.plotly_chart(fig)
        st.write("This pie chart shows the distribution of seller types (e.g., distributor vs. mandi wala). It provides insights into the makeup of your data sources.")

    elif selected_graph == "Regional Price Comparison":
        fig = px.box(df, x='Grocery Name', y='Price', color='Region', title='Regional Price Comparison')
        st.plotly_chart(fig)
        st.write("This box plot compares prices of groceries across different regions. It can help identify regional price disparities.")

    elif selected_graph == "Seasonal Price Variations":
        seasonal_avg = df.groupby(['Grocery Name', 'Season'])['Price'].mean().reset_index()
        fig = px.bar(seasonal_avg, x='Grocery Name', y='Price', color='Season', 
                     title='Seasonal Price Variations', barmode='group')
        st.plotly_chart(fig)
        st.write("This grouped bar chart shows average prices of groceries across different seasons. It highlights how prices change with seasons.")

    elif selected_graph == "Daily Entry Count":
        df['Date'] = pd.to_datetime(df['Date'])
        daily_count = df.groupby('Date').size().reset_index(name='Count')
        fig = px.line(daily_count, x='Date', y='Count', title='Daily Entry Count')
        st.plotly_chart(fig)
        st.write("This line graph shows the number of daily entries over time. It helps track user engagement and data collection frequency.")

    elif selected_graph == "Top Contributors":
        top_contributors = df['Employee Name'].value_counts().head(10)
        fig = px.bar(top_contributors, x=top_contributors.index, y=top_contributors.values, 
                     title='Top 10 Contributors')
        st.plotly_chart(fig)
        st.write("This bar graph shows the top 10 users by number of entries. It helps identify the most active contributors.")

def show():
    admin_dashboard()
