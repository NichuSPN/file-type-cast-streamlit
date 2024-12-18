from datetime import datetime
import pandas as pd
import pathlib
import streamlit as st

def get_file_extension(filename):
    file_extension = pathlib.Path(filename).suffix
    if file_extension == ".csv":
        return True, "csv"
    elif file_extension == ".json":
        return True, "json"
    elif file_extension == ".xlsx":
        return True, "xlsx"
    else:
        return False, None
    
def get_dataframe_from_file(uploaded_file):
      success, file_type = get_file_extension(uploaded_file.name)
      if success:
          uploaded_file.seek(0)
          if file_type=="csv":
              return True, pd.read_csv(uploaded_file)
          elif file_type=="json":
              return True, pd.read_json(uploaded_file)
          else:
              return True, pd.read_excel(uploaded_file)
      else:
          return False, None
      
def get_download_button(df, type):
    if type=="csv":
        return st.download_button(
            label="Download CSV",
            data=df.to_csv().encode("utf-8"),
            file_name=f"edited_data_{datetime.now():%Y-%m-%d_%H-%M-%S}.csv"
        )
    else:
        return st.download_button(
            label="Download JSON",
            data=df.to_json(orient='records').encode("utf-8"),
            file_name=f"edited_data_{datetime.now():%Y-%m-%d_%H-%M-%S}.json"
        )