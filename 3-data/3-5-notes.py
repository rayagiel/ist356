import streamlit as st
import pandas as pd

exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')

st.write(list(exams.columns))
st.dataframe(exams)

exams_by_section = exams.groupby(by=["Class_Section"]).agg([{"Class_Section": "count", "Student_Score" : "count"}])
# the index is going to be what it is grouped on which is class sections
# the class section and student score are going to be the columns and they are going to be the counts of those variables



st.title("Exam Scores")

# common problem need to rename student score to something else or it will be confusing
options = ['Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups']

e

option = st.selectbox('Select Exam:', options)