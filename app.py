import streamlit as st

st.set_page_config(layout="wide")
st.title("Power BI Dashboard")

# IMPORTANT: Ensure this is a 'Publish to Web' or 'Embed' link
pbi_url = "https://app.powerbi.com/groups/me/reports/d7f3d326-59b5-4601-94a4-339f3cab9bfd/e45a3d2025d20801154a?experience=power-bi"

# Using the standard streamlit iframe method
st.iframe(pbi_url, height=800)
