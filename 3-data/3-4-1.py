import streamlit as st
import pandas as pd
import numpy as np

from check_functions import clean_currency, detect_whale


checks = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv")



# main code

checks["total_amount_cleaned"] = checks ["total amount of check"].apply(clean_currency)
# if clean_currency took more than one value, we would need lambdas, but we dont need it here
checks["gratuity_cleaned"] = checks ["gratuity"].apply(clean_currency)
# checks["gratuity_cleaned"] = checks.apply(lambda row: clean_currency(row["gratuity"]), axis =1 )
# this applies the function to the entire dataframe applies it to each value of the assigned column in each row 
# and assigns it to a new column

# lines 23 and 24 do the exact same thing

# price per item
checks["price_per_item"] = checks["total_amount_cleaned"]/checks["total items on check"]
# price per person
checks["price_per_person"] = checks["total_amount_cleaned"]/checks["party size"]
# items per person
checks["item_per_person"] = checks["total items on check"]/checks["party size"]
# tip percentage
checks["tip_percentage"] = checks["gratuity_cleaned"]/checks["total_amount_cleaned"]

# calculating the 75th percentile
top_25_percentile_items_per_person = np.percentile(checks["item_per_person"], 75)
top_25_percentile_price_per_person = np.percentile(checks["price_per_person"], 75)

# apply kpi

checks["customer_type"] = checks.apply(lambda row: detect_whale(
    row["item_per_person"], 
    row["price_per_person"], 
    top_25_percentile_items_per_person, 
    top_25_percentile_price_per_person), axis=1)

# outputs 

st.write("==Check Data==")
st.write("The 75th percentile for items per person is: ", top_25_percentile_items_per_person)
st.write("The 75th percentile for price per person is: ", top_25_percentile_price_per_person)

customer_values = checks["customer_type"].value_counts()

cols = st.columns(len(customer_values))
for i, (customer_type, count) in customer_values.items():
    cols[i].metric(label=customer_type, value=count)

st.dataframe(checks)

