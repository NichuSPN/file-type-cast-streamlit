import streamlit as st

pages = st.navigation([
    st.Page("singlepage.py", title="No Tabs"),
    st.Page("tabs.py", title="3 Tabs")
])
    
pages.run()