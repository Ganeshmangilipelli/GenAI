import streamlit as st
import pandas as pd
st.title("Streamlit")
name = st.text_input("Enter your name")
age=st.slider("Enter your age",0,100,25)
options=["Male","Female","Other"]
gender=st.selectbox("Select your gender",options)
st.write("you selected",gender)
if name:
    st.write(f"Hello {name}")

data={
    "name":["A","B","C"],
    "age":[10,20,30]

}
df=pd.DataFrame(data)
st.dataframe(df)

upload_file=st.file_uploader("Upload a file",type=["csv","txt"])
if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.dataframe(df)
