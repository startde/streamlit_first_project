import streamlit as st
import pandas as pd

df = pd.read_csv(r"test.csv")

st.title ("Bike Sharing Demand")
st.subheader ("Raw Data")
st.dataframe(df)

weather = st.slider(
    "Выбери погоду",
    min_value=1,
    max_value=4,
    value=2,
    step=None,
)

season = st.slider(
    "Выбери время года",
    min_value=1,
    max_value=4,
    value=2,
    step=None,
)

working_day = st.slider(
    "Выбери рабочий/нерабочий день",
    min_value=0,
    max_value=1,
    value=0,
    step=None,
)

holiday = st.slider(
    "Выбери праздничный день",
    min_value=0,
    max_value=1,
    value=0,
    step=None,
)

st.subheader ("Modified Data")
st.dataframe(df.loc[((df['weather'] == weather) & (df['season'] == season) & ((df['holiday'] == holiday) & ((df['workingday'] == working_day))))])
