import streamlit as st
from utils import load_data

st.set_page_config(
    page_title="Amazon Bestseller Dashboard",
    page_icon="📚",
    layout="wide"
)

df = load_data()

st.title("📚 Amazon Bestseller Books Dashboard")

st.markdown("""
Analyze trends, ratings, reviews, prices, and authors from Amazon's Top 500 Bestselling Books dataset.
""")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Books", len(df))
col2.metric("Authors", df["Author"].nunique())
col3.metric("Avg Rating", round(df["Rating"].mean(), 2))
col4.metric("Avg Price", f"${df['Price (USD)'].mean():.2f}")

st.image(
    "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f",
    use_container_width=True
)

st.info("Use the sidebar to explore the dataset.")
