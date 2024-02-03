"""
My second app
We will use NumPy to generate a random (10,20) array and display it with labeled columns
"""

import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.table(dataframe)
