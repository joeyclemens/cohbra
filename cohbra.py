import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt
from datetime import datetime

# Set main page title
st.title("KPI Dashboard")

# Define function to create the line chart using Altair
def create_line_chart(df, title):
    # Convert Dates column to datetime type for plotting purposes
    df['Dates'] = pd.to_datetime(df['Dates'], format='%d/%m/%Y')

    # Define the line chart using Altair
    chart = alt.Chart(df).mark_line().encode(
        x=alt.X('Dates:T', 
                axis=alt.Axis(title='Date', format=("%d/%m/%Y"), tickCount=len(df.index))),
        y=alt.Y('Actual', sort=None, title='Targets'),
        tooltip=[alt.Tooltip('Dates', title='Date'), alt.Tooltip('Actual', title='Target')]
    ).properties(
        width=1000  # Set the chart width to 1000 pixels
    )

    # Add target line to chart
    target_line = alt.Chart(df).mark_line(strokeDash=[5, 5], stroke='red').encode(
        x='Dates',
        y=alt.Y('Target', sort=alt.EncodingSortField(field='Target', order='ascending')),
    )

    # Combine the two charts
    final_chart = chart + target_line

    # Set the subtitle of the chart
    st.subheader(title)

    st.altair_chart(final_chart)

    # Define the header of the table
    st.header(title)
    # Display the table
    st.write(df)



# Open image
image = Image.open('MJMEDICAL.png')

# Display image
st.image(image)

# Load data from CSV files
total_progress = pd.read_csv('total_progress.csv')
dataentry_progress = pd.read_csv('dataentry_progress.csv')
roomloading_progress = pd.read_csv('roomloading_progress.csv')
activity_progress = pd.read_csv('activity_progress.csv')
costs = pd.read_csv('costs.csv')




tables = {
    'Costs': costs,
     'Activity Progress': activity_progress
}




# Add selectbox to choose which graph and table to show
option = st.sidebar.selectbox('Select an option',
                             ['Charts', 'Costs'])

if option == 'Charts':
    charts = {
        'Total Progress': total_progress,
        'Equipment Planning Progress': dataentry_progress,
        'Room Loading Progress': roomloading_progress,
        'Activity Progress': activity_progress
    }

    chart_choice = st.sidebar.selectbox('Choose chart', list(charts.keys()))

    selected_chart = charts[chart_choice]

    create_line_chart(selected_chart, chart_choice)

elif option == 'Costs':
    
    table_choice = st.sidebar.selectbox('Costs', list(tables.keys()))
     # Count the number of times 'Cohbra' appears in the 'Cost Source Manufacturer' column
    count = len(costs[costs['Cost Source Manufacturer'] == 'Cohbra'])

    # Calculate the percentage of rows that have 'Cohbra' as the manufacturer
    total_rows = len(costs)
    percentage = (count / total_rows) * 100

      # Display the percentage of costs for the chosen manufacturer
    st.write(f"Costs are at {percentage:.2f}% completion.")
    
    

    selected_table = tables[table_choice]



    st.dataframe(selected_table)


 
