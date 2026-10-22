import streamlit as st
import pandas as pd
import numpy as np
import requests

# use requests to read in this as json "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json
url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json"
response = requests.get(url)
employee_data = response.json()

st.write(employee_data)
# loop over each key to create a dataframe and display it

# this was me figuring out how to write the code

# for department in employee_data:
#     st.write(f"Data for {department}:")
#     # employee data is the dictionary and gets the value for the key "department", for example marketing that 
#     # data is a list and each entry becomes a row
#     df = pd.DataFrame(employee_data[department]) 
#     st.dataframe(df)
    

dfs = []

for key in employee_data.keys():
    df = pd.DataFrame(employee_data[key])
    df["department"] = key
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)
st.write("Combined DataFrame")
st.dataframe(combined_df)


filename = "3-data/combined_employee_data.json"
combined_df.to_json(filename, orient = "records", lines = True)
st.write("Combined DataFrame saved to {filename} in JSON Lines Format")
# the l at the end of json is to let humans know that the format is json lines 