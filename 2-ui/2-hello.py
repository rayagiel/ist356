import streamlit as st

st.title("Saying Hello.")
name = st.text_input("And you are?")
age = st.number_input("How old are you?", min_value=0, max_value = 120, step =1)


button_state= st.button("Submit")

if button_state:
    st.write(f"Hello, {name}!")
    st.write(f"You are {age} years old.")