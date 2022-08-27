import streamlit as st

st.set_page_config(
     page_title="ADV data processing",
     page_icon="✨",
     layout="wide",
     initial_sidebar_state="expanded"
 )

st.title("Process ADV data")

st.header("Processing a single point")

with st.expander("Links and more information"):
    """
    🔎 [Nortek Vectrino: The Comprehensive Manual - Velocimeters](https://support.nortekgroup.com/hc/en-us/articles/360029839351-The-Comprehensive-Manual-Velocimeters)
    """