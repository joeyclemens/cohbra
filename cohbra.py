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

# Set the header of the table
st.header("Progress")

# Define the room information as a pandas dataframe
progress = pd.read_csv('progress.csv')

# Define the room information as a pandas dataframe
rooms = pd.read_csv('priority.csv')

# Display the tables side-by-side
col1, col2 = st.columns(2)
with col1:
    st.header("Progress")
    st.write(progress)

with col2:
    st.header("List of Priority Rooms")
    st.write(rooms)

st.header("Costs")
# import matplotlib and set style
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# create data for the pie chart
labels = ['Completed', 'Remaining']
sizes = [166, 16]
colors = ['#1f77b4', '#d62728']

# plot the pie chart
fig_pie, ax_pie = plt.subplots()
ax_pie.pie(sizes, labels=labels, colors=colors, startangle=90, autopct='%1.1f%%')
ax_pie.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# set the title of the pie chart
ax_pie.set_title('Costing Completion Percentage')

# display the pie chart in streamlit
st.write(fig_pie)






