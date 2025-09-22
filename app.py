import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv", low_memory=False)
    # Add year column
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    return df

df = load_data()

# --- App Layout ---
st.title("CORD-19 Data Explorer")
st.write("A beginner-friendly app to explore COVID-19 research papers 📊")

# Show a sample of the data
if st.checkbox("Show raw data sample"):
    st.write(df.head())

# --- Year Range Filter ---
years = df["year"].dropna().astype(int)
min_year, max_year = int(years.min()), int(years.max())
year_range = st.slider("Select Year Range", min_year, max_year, (2020, 2021))

filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

st.write(f"Showing results for **{year_range[0]}–{year_range[1]}**")
st.write(f"Number of papers: {len(filtered_df)}")

# --- Visualization 1: Publications per Year ---
st.subheader("Publications Over Time")
year_counts = filtered_df["year"].value_counts().sort_index()

fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax, palette="viridis")
ax.set_title("Number of Publications per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# --- Visualization 2: Top Journals ---
st.subheader("Top Journals")
top_journals = filtered_df["journal"].value_counts().head(10)

fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax, palette="magma")
ax.set_title("Top 10 Journals by Paper Count")
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Journal")
st.pyplot(fig)

st.success("✅ Done! Explore the dataset interactively above.")
