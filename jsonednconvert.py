from utils import ednToJSON, jsonToEdn
import streamlit as st

st.set_page_config(layout="wide")
session_state = st.session_state["jsonedn"]

if not 'json' in session_state:
    session_state['json'] = ""
    session_state['edn'] = ""
    
def jsonToEdnOnClick():
    try:
        session_state['edn']=jsonToEdn(session_state['json'])
    except Exception as error:
        st.error(error)
        
def ednToJsonOnClick():
    try:
        session_state['json']=ednToJSON(session_state['edn'])
    except Exception as error:
        st.error(error)
        
def clrOnClick():
    session_state['json'] = ""
    session_state['edn'] = ""

colJson, colEdn = st.columns(2, border=True, vertical_alignment="center", gap="medium")
colJson.subheader("JSON")
session_state['json'] = colJson.text_area(label="json_text_area", 
                                             height=600, 
                                             value=session_state['json'],
                                             label_visibility="hidden")
colEdn.subheader("EDN")
session_state['edn'] = colEdn.text_area(label="edn_text_area", 
                                           height=600, 
                                           value=session_state['edn'],
                                           label_visibility="hidden")

jte, clr, etj = st.columns([0.45, 0.35, 0.175])
jte.button(label="Convert from JSON to EDN",
           type="primary",
           on_click=jsonToEdnOnClick)
clr.button(label="CLEAR",
           type="secondary",
           on_click=clrOnClick)
etj.button(label="Convert from EDN to JSON",
           type="primary",
           on_click=ednToJsonOnClick)