import streamlit as st
import pandas as pd
import altair as alt

# Set main page title
st.title("MJM Cohbra Workshop")

# Define the data as a pandas dataframe
data = pd.DataFrame({
    'Dates': ['16/12/2022', '01/01/2023', '01/02/2023', '01/03/2023', '01/04/2023', '01/05/2023', '01/06/2023'],
    'Target': [10, 20, 30, 40, 50, 60, 69],
    'Actual': [16, 26, 29, 29, None, None, None]
})

# Convert Dates column to datetime type for plotting purposes with first day of the month
data['Dates'] = pd.to_datetime(data['Dates'], format='%d/%m/%Y').dt.strftime('%Y-%m-01')

# Define the line chart using Altair
chart = alt.Chart(data).mark_line().encode(
    x='Dates',
    y=alt.Y('Actual', sort=None, title='Targets'),
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

# Set the header of the table
st.header("Progress")

# Define the progress information and rooms information as pandas dataframes
progress = pd.read_csv('progress.csv')
rooms = pd.read_csv('priority.csv')
costs = pd.read_csv(r'costs.csv')

# Display the tables side-by-side
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Progress")
    st.write(progress)
with col2:
    st.header("List of Priority Rooms")
    st.write(rooms)
with col3:
    st.header("Costs")
    # Get total cost of each category
    cost_by_category = costs.groupby('Category')['Amount'].sum()
    # Create the pie chart using Altair
    pie_chart = alt.Chart(cost_by_category.reset_index()).mark_circle().encode(
        alt.Color('Category', legend=None),
        tooltip=['Category', 'Amount']
    ).transform_aggregate(
        Amount='sum(Amount)',
        groupby=['Category']
    ).transform_joinaggregate(
        Total='sum(Amount)'
    ).transform_calculate(
        Percent="datum.Amount / datum.Total"
    ).mark_bar().encode(
        x='Percent:Q',
        y=alt.Y('Category:N', sort='-x'),
        color='Category:N'
    )
    st.altair_chart(pie_chart, use_container_width=True)
