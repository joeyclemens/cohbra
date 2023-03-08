import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt
import numpy as np

# Set main page title
st.title("")
# Open image
image = Image.open('MJMEDICAL.png')

# Display image
st.image(image)

# Define the data as a pandas dataframe
data = pd.DataFrame({
    'Dates': ['01/03/2023', '01/04/2023', '01/05/2023', '01/06/2023'],
    'Target': [17, 35, 52, 69],
    'Actual': [8, None, None, None]
})

# Convert Dates column to datetime type for plotting purposes with first day of the month
data['Dates'] = pd.to_datetime(data['Dates'], format='%d/%m/%Y').dt.strftime('%Y-%m-01')

# Define the line chart using Altair
chart = alt.Chart(data).mark_line().encode(
    x='Dates',
    y=alt.Y('Actual',sort=None, title='Targets'),
    tooltip=[alt.Tooltip('Dates', title='Date'), alt.Tooltip('Actual', title='Target')]
)

# Add target line to chart
target_line = alt.Chart(data).mark_line(strokeDash=[5, 5], stroke='red').encode(
    x='Dates',
    y=alt.Y('Target', sort=alt.EncodingSortField(field='Target', order='ascending')),
)

# Combine the two charts
final_chart = chart + target_line

# Set the subtitle of the chart
st.subheader("Progress")

# Display the chart
st.altair_chart(final_chart, use_container_width=True)


# Create a navigation sidebar with options to jump to different sections of the page
nav = st.sidebar.radio("",["Progress","List of Priority Rooms","Equipment planning, room loading completion and Activities", "Costs"])

# Show the appropriate section based on the selected option
if nav == "Progress":
    # Define the header of the table
    st.header("Progress")
    # Define the room information as a pandas dataframe
    progress = pd.read_csv('progress.csv')
    # Display the table
    st.write(progress)
elif nav == "List of Priority Rooms":
    # Define the header of the table
    st.header("List of Priority Rooms")
    # Define the room information as a pandas dataframe
    rooms = pd.read_csv('priority.csv')
    # Display the table
    st.write(rooms)
elif nav == "Equipment planning, room loading completion and Activities":
    # Define the room information as a pandas dataframe
    datroom = pd.read_csv('dataent.csv')
    st.header("Equipment planning, room loading completion and Activities")
    st.write(datroom)
elif nav == "Costs":
    # Define the header of the table
    st.header("Costs")
    # Define the room information as a pandas dataframe
    cost = pd.read_csv('costs.csv')
    # Count the number of times 'cohbra' appears in the 'Cost Source Manufacturer' column
    count = len(cost[cost['Cost Source Manufacturer'] == 'Cohbra'])
    # Calculate the percentage of rows that have 'cohbra' as the manufacturer
    total_rows = len(cost)
    percentage = (count / total_rows) * 100
    # Display the percentage of costs for the chosen manufacturer
    st.write(f"Costs are at {percentage:.2f}% completion.")
    # Display the table
    st.write(cost)
