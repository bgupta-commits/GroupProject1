import streamlit as st

st.set_page_config(layout="wide")
st.title("Power BI Dashboard")

# IMPORTANT: Ensure this is a 'Publish to Web' or 'Embed' link
pbi_url = "https://app.powerbi.com/groups/me/reports/8ad0f7f2-1b1e-4986-a243-1f808f9ed292/e45a3d2025d20801154a?experience=power-bi"

# Using the standard streamlit iframe method
st.iframe(pbi_url, height=800)
