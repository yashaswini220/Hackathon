import streamlit as st
from utils import load_data

df = load_data()

st.title("📊 Dataset Overview")

st.subheader("Dataset Shape")

st.write(f"Rows: {df.shape[0]}")
st.write(f"Columns: {df.shape[1]}")

st.subheader("Preview")

st.dataframe(df.head(20))

st.subheader("Column Information")

st.dataframe(df.dtypes)

st.subheader("Missing Values")

st.dataframe(df.isnull().sum())

st.subheader("Statistical Summary")

st.dataframe(df.describe())
