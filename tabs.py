import streamlit as st
import pandas as pd
import pathlib
from datetime import datetime

st.divider()
st.title("File Type cast")
st.divider()

tab1, tab2, tab3 = st.tabs(["Upload", "Edit", "Download"])

with tab1:
    st.header("Upload a file (CSV, JSON or XLSX)")
    uploaded_file = st.file_uploader("Choose a file", 
                                    type=["csv", "json", "xlsx"],
                                    accept_multiple_files=False)

    def update_file_name(file):
        st.session_state["file"]=file
        suffix = pathlib.Path(file.name).suffix
        if suffix == ".csv":
            st.session_state["type"]="csv"
        elif suffix == ".json":
            st.session_state["type"]="json"
        elif suffix == ".xlsx":
            st.session_state["type"]="xlsx"
        else:
            st.error(f"Format of file {file.name} not supported\nFormat: {suffix}\nSupported Formats: .csv, .json and .xlsx")
            st.session_state["type"]=st.session_state["file"]=None
            file=None

    if uploaded_file:
        update_file_name(uploaded_file)
    else:
        st.write("Waiting for you to upload a file...")

with tab2:
    st.header("Edit the data if needed")
    if 'file' in st.session_state and st.session_state['file']!=None:
        df = None
        if st.session_state["type"]=="csv":
            df = pd.read_csv(st.session_state["file"])
        elif st.session_state["type"]=="json":
            df = pd.read_json(st.session_state["file"])
        elif st.session_state["type"]=="xlsx":
            df = pd.read_excel(st.session_state["file"])
        else:
            st.error("Something went wrong")
        st.session_state["edited_df"] = st.data_editor(df)
        st.divider()
    else:
        st.write("Data still not uploaded...")

with tab3:
    @st.fragment
    def download_section():
        st.header("Download here")
        if 'edited_df' in st.session_state:
            headingCol, dropdownCol = st.columns([0.7, 0.3], vertical_alignment="center")
            headingCol.write("Choose the format to download in")
            st.session_state["selected"] = dropdownCol.selectbox("something", label_visibility="collapsed", options=["csv", "json"])
            if st.session_state["selected"]=="csv":
                st.download_button(
                    label="Download CSV",
                    data=st.session_state["edited_df"].to_csv().encode("utf-8"),
                    file_name="{date:%Y-%m-%d_%H:%M:%S}.csv".format(date=datetime.now()))
            elif st.session_state["selected"]=="json":
                st.download_button(
                    label="Download JSON",
                    data=st.session_state["edited_df"].to_json().encode("utf-8"),
                    file_name="{date:%Y-%m-%d_%H:%M:%S}.json".format(date=datetime.now()))
        else:
            st.write("Data still not uploaded...")
    download_section()
    
    
    