import streamlit as st
from utils import get_dataframe_from_file, get_download_button

session_state = st.session_state["singlepage"]

st.divider()
st.title("File Type Cast")
st.divider()

st.header("Upload a File (CSV, JSON, or XLSX)")
uploaded_file = st.file_uploader("Choose a file", 
                                     type=["csv", "json", "xlsx"],
                                     accept_multiple_files=False)

if uploaded_file:
    success, session_state["source_df"] = get_dataframe_from_file(uploaded_file)
    if not success:
        st.error(f"Unsupported file format. Please upload a .csv, .json, or .xlsx file.")
else:
    st.write("Waiting for you to upload a file...")

st.divider()
if 'source_df' in session_state and session_state['source_df'] is not None:
    st.header("Edit the Data if Needed")
    session_state["edited_df"] = st.data_editor(session_state['source_df'])
    st.divider()

@st.fragment
def download_section():
    if 'edited_df' in session_state:
        st.header("Download Your Edited File")
        heading_col, dropdown_col = st.columns([0.7, 0.3], vertical_alignment="center")
        heading_col.write("Choose the format to download:")
        session_state["selected_format"] = dropdown_col.selectbox("Select format", options=["csv", "json"], label_visibility="collapsed")
        
        get_download_button(session_state["edited_df"], session_state["selected_format"])
        st.divider()

download_section()