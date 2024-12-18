from datetime import datetime
import pandas as pd
import pathlib, edn_format, json
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

def __get_json_key(key):
    if isinstance(key, edn_format.Keyword):
        return str(key)[1:]
    return str(key)

def __convert_to_json_serializable(obj):
    if isinstance(obj, edn_format.ImmutableDict):
        return {
            __get_json_key(key): __convert_to_json_serializable(value) 
            for key, value in obj.items()
        }
    elif isinstance(obj, edn_format.ImmutableList):
        return [__convert_to_json_serializable(item) for item in obj]
    elif isinstance(obj, edn_format.Keyword):
        return str(obj)[1:]
    elif isinstance(obj, edn_format.Symbol):
        return str(obj)
    else:
        return obj
    
def ednToJSON(edn_string):
    edn_obj = edn_format.loads(edn_string)
    json_serialized = __convert_to_json_serializable(edn_obj)
    return json.dumps(json_serialized, indent=4)
    
def __convert_to_edn(obj):
    if isinstance(obj, dict):
        return edn_format.ImmutableDict({
            edn_format.Keyword(key): __convert_to_edn(value)
            for key, value in obj.items()
        })
    elif isinstance(obj, list):
        return edn_format.ImmutableList([__convert_to_edn(item) for item in obj])
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, (int, float, bool)) or obj is None:
        return obj
    else:
        raise TypeError(f"Unsupported type: {type(obj)}")

def jsonToEdn(json_string):
    json_obj = json.loads(json_string)
    edn_formatted = __convert_to_edn(json_obj)
    return edn_format.dumps(edn_formatted, indent=4)