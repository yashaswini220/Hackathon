import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

st.title("⭐ Price & Rating Analysis")

st.subheader("Price Distribution")

fig = px.histogram(
    df,
    x="Price (USD)",
    nbins=20,
    title="Price Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Rating Distribution")

fig2 = px.histogram(
    df,
    x="Rating",
    nbins=15,
    title="Ratings Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("Price vs Rating")

fig3 = px.scatter(
    df,
    x="Price (USD)",
    y="Rating",
    color="Category",
    hover_data=["Title"],
    title="Price vs Rating"
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("Top 10 Most Reviewed Books")

top_reviews = df.nlargest(10, "Reviews")

fig4 = px.bar(
    top_reviews,
    x="Reviews",
    y="Title",
    orientation="h",
    title="Most Reviewed Books"
)

st.plotly_chart(fig4, use_container_width=True)
