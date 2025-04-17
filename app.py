import streamlit as st

import numpy as np
import pandas as pd

st.markdown("""# Hello World""")
st.markdown("""# Hello Lucas""")
spell = st.secrets['spell']
key = st.secrets.some_magic_api.key

st.write(key)
st.write(spell)

st.markdown("""# This is a header
## This is a sub header
This is text""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 50, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df

if st.checkbox('Show content'):
    st.write('''
        This code will only be executed when the check box is checked

        Streamlit elements injected inside of this block of code will \
        not get displayed unless it is checked
        ''')


def get_data():
    return pd.DataFrame(
            np.random.randn(3, 3),
            columns=['a', 'b', 'c'])

@st.cache
def get_cached_data():
    return get_data()

st.write("Uncached dataframe")
st.write(get_data())

st.write("Cached dataframe")
st.write(get_cached_data())
