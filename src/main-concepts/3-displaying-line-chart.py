"""
My third app
We will use NumPy to generate a random (20,3) array and display it as a line chart
"""

import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
