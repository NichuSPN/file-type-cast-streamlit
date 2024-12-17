import streamlit as st

st.Page("singlepage.py", title="Single Page")

st.Page("tabs.py", title="Tabbed Interface")
pages = st.navigation([
    st.Page("singlepage.py", title="Single Page"),
    st.Page("tabs.py", title="Tabbed Interface")])

pages.run()