import streamlit as st

st.title("GPA Status")
name = st.text_input("Enter you name:")
gpa = st.number_input("Enter your GPA:", min_value = 0.0, max_value = 4.0, step = 0.1)
major = st.selectbox("What is your major?",("IMT", "IST", "ADA"))

def get_status(gpa:float)->str:
    if gpa < 1.8:
        gpa_status = "Probation"
    elif gpa > 3.4:
        gpa_status = "Dean's List"
    else:
        gpa_status = "No List"
    return gpa_status

status = get_status(gpa)
button_state= st.button("Submit")
if button_state:
    st.write(f"{name.upper()} in {major.upper()} with {gpa} is on {status}.")



