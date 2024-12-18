import streamlit as st

if "singlepage" not in st.session_state:
    # Manage separate session endpoints for pages
    st.session_state["singlepage"] = {}
    st.session_state["tabs"] = {}
    st.session_state["jsonedn"] = {}

pages = st.navigation([
    st.Page("jsonednconvert.py", title="JSON-EDN Converter"),
    st.Page("singlepage.py", title="Single Page"),
    st.Page("tabs.py", title="Tabbed Interface")])

pages.run()