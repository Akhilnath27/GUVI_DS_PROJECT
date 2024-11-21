import streamlit as st
import pandas as pd
import pymysql
from datetime import timedelta

# Database connection
def get_db_connection():
    return pymysql.connect(host='127.0.0.1', user='root', passwd='Akhil@26', database='Red_bus')

# Sidebar menu
intro = st.sidebar.radio('Main Menu', ['Home page', 'Check In for Bus Routes'])

if intro == 'Home page':
    st.title('Welcome to My Webpage 🌍')
    st.subheader('Redbus Data Scraping')
    st.write('- This involves using an automated method to extract data from the Redbus website, such as bus routes, schedules, pricing, and store it in a database for analysis.')

    # Details about the project
    st.subheader('Objective of the Project')
    st.write("""Automate the collection of bus travel data from the Redbus website using Selenium. 
             This includes gathering detailed information such as:
                    \n- Bus routes
                    \n- Ratings
                    \n- Schedules
                    \n- Ticket prices
                    \n- Seat availability""")
    st.write("Store the scraped data in a structured SQL database, making it easier to access, manage, and analyze.")
    st.write("Develop a user-friendly Streamlit application to display, filter, and analyze bus routes based on various criteria.")
    st.header("Explore Bus Routes Across India 🚀")
else:
    # Helper functions
    def fetch_distinct(column_name, condition=None):
        """Fetch distinct values from the specified column."""
        myconnection = get_db_connection()
        mycursor = myconnection.cursor()
        query = f"SELECT DISTINCT {column_name} FROM bus_routes"
        if condition:
            query += f" WHERE {condition}"
        query += f" ORDER BY {column_name}"
        mycursor.execute(query)
        result = [row[0] for row in mycursor.fetchall()]
        mycursor.close()
        myconnection.close()
        return result

    def timedelta_to_str(td):
        """Convert a timedelta object to a string (HH:MM:SS)."""
        total_seconds = int(td.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    # Fetch data for filters
    route_names = fetch_distinct("route_name")
    bustypes = fetch_distinct("bus_type")
    ratings = fetch_distinct("star_rating", "star_rating IS NOT NULL")
    prices = fetch_distinct("price", "price IS NOT NULL")
    ac_types = fetch_distinct("ac_type")
    seat_types = fetch_distinct("seat_type")
    departing_times = fetch_distinct("departing_time", "departing_time IS NOT NULL")

    # Parse numeric data
    min_price, max_price = float(min(prices)), float(max(prices))
    min_rating, max_rating = float(min(ratings)), float(max(ratings))

    # Time conversion for slider
    departing_time_objs = [pd.to_datetime(timedelta_to_str(t)).time() for t in departing_times]

    # Align filters properly
    st.title("🚌 Available Bus Routes")
    st.markdown("---")

    st.subheader("🔍 Filters")
    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            selected_route = st.selectbox("Select Route", route_names)
        with col2:
            selected_price = st.slider('Bus Fare Range (₹)', min_value=min_price, max_value=max_price, value=(min_price, max_price), step=500.00)
        with col3:
            selected_rating = st.slider('Rating', min_value=min_rating, max_value=max_rating, value=(min_rating, max_rating), step=0.5)

    with st.container():
        col4, col5 = st.columns(2)
        with col4:
            selected_ac = st.radio("Type", options=ac_types, horizontal=True)
        with col5:
            selected_seat = st.radio("Seat Type", options=seat_types, horizontal=True)

    col6, col7 = st.columns([2, 2])
    with col6:
        start_time, end_time = st.slider(
            'Departing Time Range',
            min_value=min(departing_time_objs),
            max_value=max(departing_time_objs),
            value=(min(departing_time_objs), max(departing_time_objs)),
            format="HH:mm:ss"
        )

    st.markdown("---")

    # Fetch filtered data
    start_time_str = start_time.strftime("%H:%M:%S")
    end_time_str = end_time.strftime("%H:%M:%S")

    query = """
        SELECT * FROM bus_routes
        WHERE route_name = %s
        AND star_rating BETWEEN %s AND %s
        AND TIME(departing_time) BETWEEN %s AND %s
        AND price BETWEEN %s AND %s
        AND ac_type = %s
        AND seat_type = %s
    """

    myconnection = get_db_connection()
    mycursor = myconnection.cursor()
    mycursor.execute(query, (selected_route, selected_rating[0], selected_rating[1],
                             start_time_str, end_time_str, selected_price[0], selected_price[1],
                             selected_ac, selected_seat))
    data = mycursor.fetchall()
    mycursor.close()
    myconnection.close()

    # Display results
    if data:
        df = pd.DataFrame(data, columns=['id', 'route_name', 'route_link', 'bus_name', 'bus_type', 
                                         'departing_time', 'duration', 'reaching_time', 'star_rating', 
                                         'price', 'seats_available', 'ac_type', 'seat_type'])
        df = df.drop(columns=['id', 'route_link'])

        st.subheader("🚌 Available Routes")
        st.dataframe(df, use_container_width=True)
        st.success('🎉 Available Routes 🎉')
    else:
        st.error("No Buses 🚍 found for the selected filters. Try different options.")
