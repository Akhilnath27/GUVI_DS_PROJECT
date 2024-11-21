### Redbus Data Scraping with Selenium & Interactive Dynamic Filtering using Streamlit
---

### **Key Skills**
- **Web Scraping**: Leveraging Selenium to automate the collection of live bus data from the Redbus website, including government and private buses.
- **Python & SQL**: Efficient handling of scraped data, structured storage in an SQL database, and seamless integration for analysis.
- **Streamlit**: Developing an interactive and user-friendly web application to filter, visualize, and analyze bus route data.

---

### **Problem Overview**
- **Automation**: Extract detailed travel information (e.g., routes, schedules, prices, seat availability, ratings) from Redbus.
- **Data Storage**: Maintain scraped data in a structured SQL database for easy accessibility and management.
- **User Interaction**: Create an intuitive Streamlit-based application for filtering and analyzing bus data dynamically.

---

### **Use Cases**
1. **Travel Aggregators**: Offer real-time information on schedules and seat availability for end-users.  
2. **Market Analysis**: Analyze travel patterns for strategic insights and research.  
3. **Customer Experience**: Enable tailored travel options based on individual preferences.  
4. **Competitor Benchmarking**: Compare pricing, bus ratings, and services for competitive positioning.

---

### **Data Scraping Process**
1. **Routes Extraction**: Use Selenium to extract route-specific data such as starting and ending locations, and total travel distance.  
2. **Bus Details**: Collect additional information like departure times, ratings, prices, AC/Non-AC types, and seat availability for each route.

---

### **SQL Database Schema**
The database schema includes essential fields such as:
- **Route Details**: Name, originating and destination points.  
- **Bus Details**: Bus type, star ratings, departure time, ticket price, AC/Non-AC type, and seat availability.  
- **Primary Key**: An auto-incrementing primary key ensures efficient querying and data management.

---

### **Streamlit Application Features**
1. **Filter Options**:  
   - **Route Selection**: Choose routes dynamically.  
   - **Price Range**: Adjustable sliders for budget-friendly options.  
   - **Ratings**: Filter by bus ratings for better quality selection.  
   - **AC/Non-AC**: Toggle between AC and Non-AC buses.  
   - **Seat Type**: Select sleeper or seater buses.  
   - **Departure Time Range**: Refine results based on travel time preferences.  

2. **Interactive Design**:  
   - Dropdown menus, sliders, and radio buttons for smooth user interaction.  
   - Filter and view the results in real-time with a responsive layout.  

3. **Dynamic Querying**:  
   - SQL queries are dynamically generated based on user inputs, ensuring precise and relevant results.  

4. **Results Display**:  
   - A clean and scrollable data table showcasing the filtered results, including departure time, duration, rating, price, and seat availability.

---

### **In Summary**
This project exemplifies a seamless integration of **web scraping**, **database management**, and **interactive web application development**. By automating data extraction, efficiently storing and managing it in a database, and providing a user-friendly Streamlit app, it addresses the needs of travel aggregators, researchers, and customers alike. This solution is impactful for the transportation sector, enabling real-time analysis, enhanced customer service, and market competitiveness.

![Screenshot 2024-11-21 122115](https://github.com/user-attachments/assets/513adb2a-3023-4ac4-97f5-012c734bba44)
![Screenshot 2024-11-21 122131](https://github.com/user-attachments/assets/06b92bb1-4a34-4aed-929a-aa867b191c2b)

