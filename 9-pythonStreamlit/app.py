import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit")
st.write("Hello world")

st.write("this is simple text")

df=pd.DataFrame({
    "first column":[1,2,3,4],
    "second column":[10,20,30,40]
})

## create a line chart
chart_data=pd.DataFrame(
    np.random.randn(50,3),
    columns=["a","b","c"]
)

st.line_chart(chart_data)
st.write(df)

st.write("this is a dataframe")