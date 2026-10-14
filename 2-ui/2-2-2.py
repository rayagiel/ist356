# the use case for session state is only when you need to remember the value between interactions, between runs of the 
# program

# write the UI first, then shove the code and functionality on the back end
import streamlit as st

st.title("Order Amount Accumulator")

# initialize into session state
if "total_order" not in st.session_state:
    st.session_state.total_order = 0.0
    st.session_state.order_history = []


amount = st.number_input("Enter an amount", min_value = 0.0)
add_to_order = st.button("Add to Order", type="primary")
clear_order = st.button("Clear Order", type="secondary")

# order accumulation logic
if add_to_order:
    st.session_state.total_order += amount
    st.session_state.order_history.append(amount)
if clear_order:
    st.session_state.total_order = 0.0
    st.session_state.order_history = []

st.text(f"Total Order: {st.session_state.total_order}")
for o in st.session_state.order_history:
    st.text(f"Order item: {o}")
st.text(f"Order History: {st.session_state.order_history}")
