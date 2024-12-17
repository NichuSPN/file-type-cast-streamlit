import streamlit as st

@st.fragment
def singlepage():
    return st.Page("singlepage.py", title="Single Page")

@st.fragment
def tabbed():
    return st.Page("tabs.py", title="Tabbed Interface")
pages = st.navigation([
    singlepage(),
    tabbed()])

pages.run()