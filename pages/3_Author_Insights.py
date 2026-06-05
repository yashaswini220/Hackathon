import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

st.title("✍️ Author Insights")

top_authors = df["Author"].value_counts().head(15)

fig = px.bar(
    x=top_authors.values,
    y=top_authors.index,
    orientation="h",
    title="Authors with Most Bestselling Books"
)

st.plotly_chart(fig, use_container_width=True)

selected_author = st.selectbox(
    "Select Author",
    sorted(df["Author"].unique())
)

author_books = df[df["Author"] == selected_author]

st.subheader(f"Books by {selected_author}")

st.dataframe(
    author_books[
        [
            "Title",
            "Category",
            "Rating",
            "Reviews",
            "Price (USD)"
        ]
    ]
)

avg_rating = author_books["Rating"].mean()

st.metric(
    "Average Author Rating",
    round(avg_rating, 2)
)
