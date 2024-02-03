"""
My fifth app
We now get into Widgets, including:
1. Text Input
2. Slider Input
3. Checkboxes
4. Selectboxes
"""

import streamlit as st
import numpy as np
import pandas as pd

# Part 1: Text Input Widget
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name


# Part 2: Slider Input Widget
x = st.slider('x')  # this is a widget
st.write(x, 'squared is', x * x)


# Part 3: Checkbox to show/hide data
if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    chart_data

# Part 4: Selectbox for options
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    "Which number do you like best?",
    df["first column"]
)

st.write("You selected:", option)
