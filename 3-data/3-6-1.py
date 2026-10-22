# 4 polling days, 4 polls per day, 1 response per poll
import streamlit as st
import pandas as pd
import datetime

base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/"
# import roster
roster = pd.read_csv(base + "roster.csv")

# import all polls
start_date = datetime.date(2024, 1, 8)
class_split = datetime.timedelta(days=7)

# import all polls in polls_concat
polls = []
for i in range(4):
    file_date = start_date + i*class_split
    file_date_string = datetime.datetime.strftime(file_date, "%Y-%m-%d")
    filename = f"poll_responses-{file_date_string}.csv"
    filename = f"poll-responses-{file_date_string}.csv"
    st.write(f"Importing {filename}...")
    poll = pd.read_csv(base + filename)
    poll["poll_date"] = file_date
    poll["poll-filename"] = filename
    polls.append(poll)

polls_concat = pd.concat(polls)
    
# merge polls with polls_concat
polls_merged = pd.merge(roster, polls_concat, how = "left", left_on = "netid", right_on = "student_id")
# left is important because then you get everyone on the roster, even if they did not respond to a poll
# if you do inner, you will only get the students who responded to a poll
# if you do right, you will only get the students who responded to a poll, and not everyone on the roster
# activity data (polling) is always joined to the reference data (roster) so you know who did not do the activity

# use pivot table so roster data is in the row and poll_data value sare in teh columns, and the values are the count
# of the poll responses

polls_pivot = polls_merged.pivot_table(index =["netid","name"], columns = "poll_date", 
                                        values = "answer", aggfunc = "count", fill_value = 0)
st.dataframe(polls_pivot)

# now melt 
polls_melted = polls_pivot.reset_index().melt(id_vars = ["netid","name"], var_name = "poll_date", value_name = "response_count")
st.dataframe(polls_melted)


