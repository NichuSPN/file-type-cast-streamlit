import streamlit as st
import pandas as pd
import pathlib
from datetime import datetime

st.divider()
st.title("File Type Cast")
st.divider()

tab_upload, tab_edit, tab_download = st.tabs(["Upload", "Edit", "Download"])

with tab_upload:
    st.header("Upload a File (CSV, JSON, or XLSX)")
    uploaded_file = st.file_uploader("Choose a file", 
                                      type=["csv", "json", "xlsx"],
                                      accept_multiple_files=False)

    def update_file_info(file):
        st.session_state["uploaded_file"] = file
        file_extension = pathlib.Path(file.name).suffix
        if file_extension == ".csv":
            st.session_state["file_type"] = "csv"
        elif file_extension == ".json":
            st.session_state["file_type"] = "json"
        elif file_extension == ".xlsx":
            st.session_state["file_type"] = "xlsx"
        else:
            st.error(f"Unsupported file format: {file_extension}. Please upload a .csv, .json, or .xlsx file.")
            st.session_state["file_type"] = st.session_state["uploaded_file"] = None

    if uploaded_file:
        update_file_info(uploaded_file)
    else:
        st.write("Waiting for you to upload a file...")

with tab_edit:
    st.header("Edit the Data if Needed")
    if 'uploaded_file' in st.session_state and st.session_state['uploaded_file'] is not None:
        data_frame = None
        if st.session_state["file_type"] == "csv":
            data_frame = pd.read_csv(st.session_state["uploaded_file"])
        elif st.session_state["file_type"] == "json":
            data_frame = pd.read_json(st.session_state["uploaded_file"])
        elif st.session_state["file_type"] == "xlsx":
            data_frame = pd.read_excel(st.session_state["uploaded_file"])
        else:
            st.error("An error occurred while reading the file.")
        
        st.session_state["tab_edited_data_frame"] = st.data_editor(data_frame)
        st.divider()
    else:
        st.write("Data still not uploaded...")

with tab_download:
    @st.fragment
    def download_section():
        st.header("Download Your Edited File")
        if 'tab_edited_data_frame' in st.session_state:
            heading_col, dropdown_col = st.columns([0.7, 0.3], vertical_alignment="center")
            heading_col.write("Choose the format to download:")
            st.session_state["selected_format"] = dropdown_col.selectbox("Select format", options=["csv", "json"], label_visibility="collapsed")
            
            if st.session_state["selected_format"] == "csv":
                st.download_button(
                    label="Download CSV",
                    data=st.session_state["tab_edited_data_frame"].to_csv().encode("utf-8"),
                    file_name=f"edited_data_{datetime.now():%Y-%m-%d_%H-%M-%S}.csv"
                )
            elif st.session_state["selected_format"] == "json":
                st.download_button(
                    label="Download JSON",
                    data=st.session_state["tab_edited_data_frame"].to_json().encode("utf-8"),
                    file_name=f"edited_data_{datetime.now():%Y-%m-%d_%H-%M-%S}.json"
                )
        else:
            st.write("Data still not uploaded...")

    download_section()