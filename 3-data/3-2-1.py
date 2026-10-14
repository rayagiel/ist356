# 3-2-1
# three rows of headers
# first row = 4
# row delimiter = \n
#cell/ field delimiter = " "


import streamlit as st
import pandas as pd
import numpy as np


url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log"
data = pd.read_csv(url, skiprows = 3, sep = " ")
                   

st.dataframe(data)





# just other stuff 
col1 = ["A","B", "C","D"]
col2 = ["D", "C","A","B"]
same = set(col1) == set(col2)
# ensures the order of columns is the same across 

