import pandas as pd
import streamlit as st
df=pd.read_csv("Automobile.csv")
st.dataframe(df)
st.bar_chart(data=df,)

