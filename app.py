import streamlit as st
import streamlit.components.v1 as components

# Set page to wide mode to better fit the dashboard
st.set_page_config(layout="wide")

st.title("My Power BI Dashboard")

# Your Power BI link goes here
pbi_url = "https://app.powerbi.com/groups/me/reports/8ad0f7f2-1b1e-4986-a243-1f808f9ed292/e45a3d2025d20801154a?experience=power-bi"

# Embed the dashboard
components.iframe(pbi_url, height=800, scrolling=True)
