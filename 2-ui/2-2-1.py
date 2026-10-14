import streamlit as st

st.title("Area/Perimeter Calculator")
length = st.number_input("Length", min_value = 0.0, max_value = 100.0, step = 1.0)
width = st.number_input("Width", min_value = 0.0, max_value = 100.0, step = 1.0)

col1, col2 = st.columns(2)
with col1:
    clear = st.button("Clear")
with col2:
    calculate = st.button("Calculate")

if clear:
    length = 0.0
    width = 0.0

if calculate:
    perimeter = 2 * (length + width)
    area = length * width
    st.success(f"Area: {area}, Perimeter: {perimeter}")

