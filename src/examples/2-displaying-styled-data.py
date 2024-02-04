"""
My second app
We use NumPy to generate a random (10,20) array and display it
with labeled columns and a Pandas Styler object to highlight some elements
"""

import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
