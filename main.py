import streamlit as st

if "singlepage" not in st.session_state:
    # Manage separate session endpoints for pages
    st.session_state["singlepage"] = {}
    st.session_state["tabs"] = {}

pages = st.navigation([
    st.Page("singlepage.py", title="Single Page"),
    st.Page("tabs.py", title="Tabbed Interface")])

pages.run()