"""
My sixth app
We now get into Layouts for Streamlit apps
We can customize the sidebar with widgets and place widgets side-by-side using columns
"""

import streamlit as st

# Add a selectbox to the sidebar
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home Phone", "Mobile Phone")
)

# Add a slider to the sidebar
add_slider = st.sidebar.slider(
    "Select a range of values",
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)

# You can use a column just like st.sidebar
left_column.button("Press Me!")

# or, even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        "Sorting Hat",
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
    )
    st.write(f"You are in {chosen} house!")
