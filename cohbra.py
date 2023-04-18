import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt
from datetime import datetime
# 4from st_aggrid import AgGrid





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
        width=900  # Set the chart width to 900 pixels
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
total_progress = pd.read_csv('progress/total_progress.csv')
total_progress_with_specs_and_cost = pd.read_csv('progress/total_progress with specs and cost.csv')
dataentry_progress = pd.read_csv('progress/dataentry_progress.csv')
roomloading_progress = pd.read_csv('progress/roomloading_progress.csv')
activity_progress = pd.read_csv('progress/activity_progress.csv')
cost_progress = pd.read_csv('progress/cost_progress.csv')
###################
priority = pd.read_csv('dataent.csv')
costs = pd.read_csv('costs.csv')
cost_total = pd.read_csv('cost_progress_total.csv')
costs_to_do = pd.read_csv('costs_to_do.csv')
specs = pd.read_csv('specs.csv')
spec_progress = pd.read_csv('progress/spec_progress.csv')
spec_room_progress = pd.read_csv('progress/spec_room_progress.csv')
overall = pd.read_csv('overall.csv')
overall_header = pd.read_csv('overall_header.csv')

    
tables = {
    'Total Room completion' : overall,
    'Costs' : costs_to_do,
    'Specs' : specs,
    'Priority Rooms':priority
}



# Add textbox to sidebar
# Add textbox to sidebar
st.sidebar.markdown("<u>Links:</u>", unsafe_allow_html=True)
# Add hyperlink to sidebar
st.sidebar.write('<a href="https://mjmedical.sharepoint.com/:x:/s/COHBRA/Eb4o_yhqVspHjEDxC7hptYYBy4ryOXYl8nmXwHW0wT12Vw?e=tzJZid" style="color: orange; text-decoration: none;">KPI Tracker</a>', unsafe_allow_html=True)
# Add a dividing line
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# Add selectbox to choose which graph and table to show
option = st.sidebar.selectbox('Select an option',
                             ['Charts', 'Tables'])

if option == 'Charts':
    charts = {
        'Total Room Progress (Equipment, Room loading, Activities)': total_progress,
        'Total Room Progress (Equipment, Room loading, Activities, Specs and Costs)': total_progress_with_specs_and_cost,
        'Equipment Planning Progress': dataentry_progress,
        'Room Loading Progress': roomloading_progress,
        'Activity Progress': activity_progress,
        'Cost left to do': cost_progress,
        'Rooms with all costs done' : cost_total,
        'Specs' : spec_progress,
        'Rooms with all specs done' : spec_room_progress
    }

    chart_choice = st.sidebar.selectbox('Choose chart', list(charts.keys()))

    selected_chart = charts[chart_choice]

    create_line_chart(selected_chart, chart_choice)

elif option == 'Tables':
   
    table_choice = st.sidebar.selectbox('Choose Table', list(tables.keys()))
    selected_table = tables[table_choice]

    st.markdown(f"## {table_choice}", unsafe_allow_html=True)

    st.table(selected_table)

# Add a dividing line
st.sidebar.markdown("<hr>", unsafe_allow_html=True)
# Add textbox to sidebar
st.sidebar.markdown("<u>Areas needing most attention:</u>", unsafe_allow_html=True)
# Add hyperlink to sidebar
st.sidebar.write('<a href="https://mjmedical.sharepoint.com/:x:/s/COHBRA/Eb4o_yhqVspHjEDxC7hptYYBy4ryOXYl8nmXwHW0wT12Vw?e=tMaVJw&nav=MTVfezc5MUFEMjVBLTdDMUMtNEJERS1CRjU1LUM0QUMxQjgxQzcwRX0" style="color: orange; text-decoration: none;">• Specs</a>', unsafe_allow_html=True)