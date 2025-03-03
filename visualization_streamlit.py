import pandas as pd
import sqlite3
import streamlit as st

# Load the data from the SQLite database
conn = sqlite3.connect('master_database.db')
df = pd.read_sql_query("SELECT * FROM master_table", conn)
conn.close()

# Streamlit app
st.title("Database Visualization")

# Filter by column
column = st.selectbox("Select column to filter by:", df.columns)
value = st.text_input("Enter filter value:")

# Apply filter
if value:
    filtered_df = df[df[column].astype(str).str.contains(value, case=False, na=False)]
else:
    filtered_df = df

# Display filtered data
st.write(f"Filtered Data (Column: {column}, Value: {value})")
st.dataframe(filtered_df)
