import requests
import pandas as pd
import numpy as np
import streamlit as st

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees.json"
response = requests.get(url)
json_data = response.json()

df = pd.json_normalize(json_data,record_path = "employees", meta = [["dept"]] )

df