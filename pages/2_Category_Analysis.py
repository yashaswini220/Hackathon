import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

st.title("📚 Category Analysis")

category_counts = df["Category"].value_counts()

fig = px.pie(
    values=category_counts.values,
    names=category_counts.index,
    title="Books by Category"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Top Sub Genres")

subgenre_counts = df["Sub-Genre"].value_counts().head(15)

fig2 = px.bar(
    x=subgenre_counts.index,
    y=subgenre_counts.values,
    labels={"x":"Sub Genre","y":"Count"},
    title="Top 15 Sub Genres"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("Format Distribution")

format_counts = df["Format"].value_counts()

fig3 = px.bar(
    x=format_counts.index,
    y=format_counts.values,
    title="Book Formats"
)

st.plotly_chart(fig3, use_container_width=True)
