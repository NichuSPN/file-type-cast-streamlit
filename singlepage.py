import streamlit as st
import pandas as pd
import pathlib
from datetime import datetime

st.divider()
st.title("File Type Cast")
st.divider()

st.header("Upload a File (CSV, JSON, or XLSX)")
uploaded_file_tab = st.file_uploader("Choose a file", 
                                     type=["csv", "json", "xlsx"],
                                     accept_multiple_files=False)

def update_file_info(file):
    st.session_state["uploaded_file_tab"] = file
    file_extension = pathlib.Path(file.name).suffix
    if file_extension == ".csv":
        st.session_state["file_type_tab"] = "csv"
    elif file_extension == ".json":
        st.session_state["file_type_tab"] = "json"
    elif file_extension == ".xlsx":
        st.session_state["file_type_tab"] = "xlsx"
    else:
        st.error(f"Unsupported file format: {file_extension}. Please upload a .csv, .json, or .xlsx file.")
        st.session_state["file_type_tab"] = st.session_state["uploaded_file_tab"] = None

if uploaded_file_tab:
    update_file_info(uploaded_file_tab)
else:
    st.write("Waiting for you to upload a file...")

st.divider()
if 'uploaded_file_tab' in st.session_state and st.session_state['uploaded_file_tab'] is not None:
    data_frame = None
    if st.session_state["file_type_tab"] == "csv":
        data_frame = pd.read_csv(st.session_state["uploaded_file_tab"])
    elif st.session_state["file_type_tab"] == "json":
        data_frame = pd.read_json(st.session_state["uploaded_file_tab"])
    elif st.session_state["file_type_tab"] == "xlsx":
        data_frame = pd.read_excel(st.session_state["uploaded_file_tab"])
    else:
        st.error("An error occurred while reading the file.")
    
    st.header("Edit the Data if Needed")
    st.session_state["edited_data_frame"] = st.data_editor(data_frame)
    st.divider()

@st.fragment
def download_section():
    if 'edited_data_frame' in st.session_state:
        st.header("Download Your Edited File")
        heading_col, dropdown_col = st.columns([0.7, 0.3], vertical_alignment="center")
        heading_col.write("Choose the format to download:")
        st.session_state["selected_format"] = dropdown_col.selectbox("Select format", options=["csv", "json"], label_visibility="collapsed")
        
        if st.session_state["selected_format"] == "csv":
            st.download_button(
                label="Download CSV",
                data=st.session_state["edited_data_frame"].to_csv().encode("utf-8"),
                file_name=f"edited_data_{datetime.now():%Y-%m-%d_%H-%M-%S}.csv"
            )
        elif st.session_state["selected_format"] == "json":
            st.download_button(
                label="Download JSON",
                data=st.session_state["edited_data_frame"].to_json().encode("utf-8"),
                file_name=f"edited_data_{datetime.now():%Y-%m-%d_%H-%M-%S}.json"
            )
        st.divider()

download_section()