import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt
from datetime import datetime
# from st_aggrid import AgGrid

st.set_page_config(page_title="KPI Tracker",
                   layout="wide")
                   

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



# Open image
image = Image.open('MJMEDICAL.png')



# easter egg link URL
link_url = "https://youshouldreallybedoingsomework.netlify.app/"

# Display title as a link
st.markdown(f'<a href="{link_url}" style="color: white; text-decoration: none;"><h1>KPI Dashboard</h1></a>', unsafe_allow_html=True)

##########CSV FILES LOAD#################

# Load data from CSV files
total_progress = pd.read_csv('progress/total_progress.csv')
total_progress_with_specs_and_cost = pd.read_csv('progress/total_progress with specs and cost.csv')
dataentry_progress = pd.read_csv('progress/dataentry_progress.csv')
roomloading_progress = pd.read_csv('progress/roomloading_progress.csv')
activity_progress = pd.read_csv('progress/activity_progress.csv')
cost_progress = pd.read_csv('progress/cost_progress.csv')
activity_room_progress = pd.read_csv('progress/activity_room_progress.csv')

###################
costs = pd.read_csv('costs.csv')
cost_total = pd.read_csv('progress/cost_progress_total.csv')
costs_to_do = pd.read_csv('costs_to_do.csv')
specs = pd.read_csv('specs.csv')
spec_progress = pd.read_csv('progress/spec_progress.csv')
spec_room_progress = pd.read_csv('progress/spec_room_progress.csv')
overall = pd.read_csv('overall.csv')
overall_audit = pd.read_csv('overall_audit.csv')
Priority_Rooms = pd.read_csv('priority.csv')

##################
spec_audit = pd.read_csv('audit/spec_audit_progress.csv')
data_audit = pd.read_csv('audit/dataentry_audit_progress.csv')
activities_audit = pd.read_csv('audit/activities_audit_progress.csv')
room_loading_audit = pd.read_csv('audit/room_loading_audit_progress.csv')

    
#tables = {
#    'Total Room completion' : overall,
#    'Costs' : costs,
#    #'Specs' : specs,
#    'Priority Rooms': Priority_Rooms,
#    'Audit' : overall_audit,
#}

########## Side bar ################

# Add textbox to sidebar
# Add textbox to sidebar
st.sidebar.markdown("<u>Links:</u>", unsafe_allow_html=True)
# Add hyperlink to sidebar
st.sidebar.write('<a href="https://mjmedical.sharepoint.com/:x:/s/COHBRA/Eb4o_yhqVspHjEDxC7hptYYBy4ryOXYl8nmXwHW0wT12Vw?e=tzJZid" style="color: black; text-decoration: none;"><b>KPI Tracker</b></a>', unsafe_allow_html=True)
# Add a dividing line
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# Add textbox to sidebar
#st.sidebar.markdown("<u>Areas needing most attention:</u>", unsafe_allow_html=True)
# Add hyperlink to sidebar
#st.sidebar.write('<a href="https://mjmedical.sharepoint.com/:x:/s/COHBRA/Eb4o_yhqVspHjEDxC7hptYYBy4ryOXYl8nmXwHW0wT12Vw?e=tMaVJw&nav=MTVfezc5MUFEMjVBLTdDMUMtNEJERS1CRjU1LUM0QUMxQjgxQzcwRX0" style="color: black; text-decoration: none;"><b>• Specs</b></a>', unsafe_allow_html=True)
# Add a dividing line
#st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# Add selectbox to choose which graph and table to show
option = st.sidebar.selectbox('Select an option',
                             ['Room Progress','Progress','Audit'])

#Room progress drop down options
if option == 'Room Progress':
    charts = {
        'Total Room Progress (Equipment, Room loading, Activities & Costs)': total_progress,
        #'Total Room Progress (Equipment, Room loading, Activities, Specs and Costs)': total_progress_with_specs_and_cost,
        'Rooms with all equipment planning done' : dataentry_progress,
        'Rooms with all room loading done' : roomloading_progress,
        'Rooms with all activities done' : activity_room_progress,
        'Rooms with all costs done' : cost_total,
        #'Rooms with all specs done' : spec_room_progress
    }

    chart_choice = st.sidebar.selectbox('Choose chart', list(charts.keys()))

    selected_chart = charts[chart_choice]

    create_line_chart(selected_chart, chart_choice)

#Individual areas progress drop down options
elif option == 'Progress':
    charts = {
        'Equipment Planning Progress': dataentry_progress,
        'Room Loading Progress': roomloading_progress,
        'Activity Progress': activity_progress,
        'Cost': cost_progress,
        #'Specs' : spec_progress,
        
    }

    chart_choice = st.sidebar.selectbox('Choose chart', list(charts.keys()))

    selected_chart = charts[chart_choice]

    create_line_chart(selected_chart, chart_choice)

#Various tables drop down options
#elif option == 'Tables':
#    table_choice = st.sidebar.selectbox('Choose Table', list(tables.keys()))
#    selected_table = tables[table_choice]

#    st.markdown(f"## {table_choice}", unsafe_allow_html=True)

#    st.table(selected_table)
    
#audit progress drop down options
elif option == 'Audit':
    charts = {
        'Equipment planning' :data_audit,
        #'Specs' : spec_audit,
        'Activities' : activities_audit, 
        'Room Loading' : room_loading_audit,
        
    }

    chart_choice = st.sidebar.selectbox('Choose chart', list(charts.keys()))

    selected_chart = charts[chart_choice]

    create_line_chart(selected_chart, chart_choice)    


    


   



    

#CSS styling for the page
#Mostly hides the stock header and footers
#But also links to a seperate style sheet

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

style_css = """
<link rel="stylesheet" href="static\style.css">
""" 
st.markdown(style_css, unsafe_allow_html=True)

