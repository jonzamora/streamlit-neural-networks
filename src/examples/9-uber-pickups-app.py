"""
Uber Pickups App for New York City, built with Streamlit
"""


import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber Pickups in New York City 🚕")

# Step 1: Fetch Data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache_data
def load_data(n_rows):
    data = pd.read_csv(DATA_URL, nrows=n_rows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data_load_state = st.text("Loading data...")
data = load_data(10_000)  # Load 10,000 rows of data into a dataframe
data_load_state.text("Loading data... Done! ⚡️")

# Step 2: (optionally) Display Raw Data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)

# Step 3: Display Histogram of Data
st.subheader("Number of Pickups by Hour")
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Step 4: Display Data from any hour of the day on a Map
hour_to_filter = st.slider("Hour", min_value=0, max_value=23, value=17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f"Map of all Pickups at {hour_to_filter}:00")
st.map(filtered_data)
