import streamlit as st
import pandas as pd

exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')

st.title("Universal Pivot Table Example")
# inputs 
row_col_vals = ['Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade']
measure_vals = ['Student_Score', 'Completion_Time']

row = st.multiselect("Select Row", options = row_col_vals)
column = st.selectbox("Select Column", options = row_col_vals)
measure = st.selectbox("Select Measure", options = measure_vals)

# process
try:
    universal_pivot_table1 = exams.pivot_table(index = row, columns = column, values = measure, aggfunc="mean")
    # outputs
    st.write(f" Pivot Table: Row: `{row}`, Column: `{column}`, Measure: `{measure}` as the mean")
    st.dataframe(universal_pivot_table1)
except ValueError as e:
    st.error(f"Row and Column must not use the same value. Error: {e}")