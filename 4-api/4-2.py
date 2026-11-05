import requests
import dotenv
import os
import streamlit as st
import pandas as pd
import json
from extractors import extract_entities

dotenv.load_dotenv()

st.title("Entity Extraction")
text = st.text_area("Enter text to extract entities:", "")
if text:
    entities = extract_entities(text)
    df = pd.json_normalize(entities)
    st.dataframe(df)

