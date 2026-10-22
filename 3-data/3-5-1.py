import streamlit as st
import pandas as pd

exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')

st.write(list(exams.columns))
st.dataframe(exams)

#df2 = exams.groupby(by=["Did_Exam_Prep Assignment"])\
 #   .agg({"Exam_Version": "count", "Student_Score": "mean"})
#df2 = df2.rename(columns={'Exam_Version': 'Student Count', 'Student_Score': 'Mean_Student_Score'})

#st.dataframe(df2)

# Get average scores by section and exam version:
avg_scores_by_section_and_version = exams.groupby(by=['Class_Section', 'Exam_Version']).agg({'Student_Score': 'mean'})

# add section and exam version back to dataframe
avg_scores_by_section_and_version['Class_Section'] = avg_scores_by_section_and_version.index.get_level_values('Class_Section')
avg_scores_by_section_and_version['Exam_Version'] = avg_scores_by_section_and_version.index.get_level_values('Exam_Version')
# reset the index
avg_scores_by_section_and_version = avg_scores_by_section_and_version.reset_index(drop=True)
#rename the Student_score to average score
avg_scores_by_section_and_version =  avg_scores_by_section_and_version.rename(columns={'Student_Score': 'Average_Score'})
#reorder the columns
avg_scores_by_section_and_version = avg_scores_by_section_and_version[['Class_Section', 'Exam_Version', 'Average_Score']]

st.dataframe(avg_scores_by_section_and_version)

# a pivot is a groupby in two dimensions, which means you need a column and a row and an aggregate
# pivot and melt they just reshape, there is no aggregate 
# in pivot table, you can reshape and aggregate at the same time, in pivot you can only reshape,
#  you need to aggregate first and then reshape

# pivot
pivot1 = avg_scores_by_section_and_version.pivot(index='Class_Section', columns='Exam_Version', values='Average_Score')
st.dataframe(pivot1)
# melt does the opposite of pivot and you can switch the rows and columns

melted1 = pivot1.reset_index().melt(id_vars = "Class_Section", value_name = "Average_Score", var_name = "Exam_Version")
st.dataframe(melted1)
# you need to reset the index before melting, otherwise the index will be used as a column in the melted dataframe
# because the index was section (M01) and it would not work


# pivot table allows you to group and pivot at the same time

# pivot table exams in row Class_Section, in columns Exam_Version, values Student_Score, aggfunc mean
st.write("Pivot Table")

pivot_table1 = exams.pivot_table(index="Class_Section", columns = "Exam_Version", values="Student_Score", aggfunc="mean")
st.dataframe(pivot_table1)