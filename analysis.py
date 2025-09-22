# final_project.py
# CORD-19 Metadata Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# PART 1: DATA LOADING AND BASIC EXPLORATION

print("Pandas imported...")

# Load the dataset
df = pd.read_csv("metadata.csv", low_memory=False)
print("CSV loaded successfully")

# Display the first 5 rows
print(df.head())

# Shape of the dataset (rows, columns)
print("Shape:", df.shape)

# Data types of each column
print("Data Types:\n", df.dtypes)

# Missing values per column
print("Missing Values:\n", df.isnull().sum())

# Basic statistics (only for numerical columns)
print("Statistics:\n", df.describe())

# PART 2: DATA CLEANING AND PREPARATION

# Check available column names
print(df.columns.tolist())

# Missing values per column
print("Missing Values:\n", df.isnull().sum())

# Drop columns with too many missing values (e.g., more than 50%)
threshold = len(df) * 0.5
df_clean = df.dropna(axis=1, thresh=threshold)

# For remaining missing values:
# - Fill numerical columns with median
num_cols = df_clean.select_dtypes(include=['number']).columns
df_clean[num_cols] = df_clean[num_cols].fillna(df_clean[num_cols].median())

# - Fill categorical/text columns with a placeholder
cat_cols = df_clean.select_dtypes(include=['object']).columns
df_clean[cat_cols] = df_clean[cat_cols].fillna("Unknown")

print("After cleaning:", df_clean.isnull().sum())

# Convert publish_time to datetime
df_clean["publish_time"] = pd.to_datetime(df_clean["publish_time"], errors="coerce")

# Extract year from publish_time
df_clean["year"] = df_clean["publish_time"].dt.year

# Add abstract word count
df_clean["abstract_word_count"] = df_clean["abstract"].apply(
    lambda x: len(str(x).split()) if x != "Unknown" else 0
)

# PART 3: DATA ANALYSIS AND VISUALIZATION

print("\n=== Data Analysis & Visualization ===")

# 1. Count papers by publication year
year_counts = df_clean["year"].value_counts().sort_index()
print("Publications by Year:\n", year_counts)

plt.figure(figsize=(8,5))
year_counts.plot(kind="bar")
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.tight_layout()
plt.show()

# 2. Identify top journals publishing COVID-19 research
top_journals = df_clean["journal"].value_counts().head(10)
print("Top Journals:\n", top_journals)

plt.figure(figsize=(8,5))
sns.barplot(x=top_journals.values, y=top_journals.index)
plt.title("Top 10 Journals")
plt.xlabel("Number of Publications")
plt.ylabel("Journal")
plt.tight_layout()
plt.show()

# 3. Most frequent words in titles (simple frequency)
from collections import Counter
import re

# Combine all titles into one big string
titles_text = " ".join(df_clean["title"].astype(str))

# Tokenize (split into words, remove short words and non-alphabetic)
words = re.findall(r"\b[a-zA-Z]{4,}\b", titles_text.lower())

# Count word frequencies
word_freq = Counter(words)

# Take the 20 most common words
common_words = word_freq.most_common(20)
print("Most Frequent Words in Titles:\n", common_words)

# Convert to DataFrame for plotting
words_df = pd.DataFrame(common_words, columns=["word", "count"])

plt.figure(figsize=(10,6))
sns.barplot(x="count", y="word", data=words_df, palette="viridis")
plt.title("Top 20 Most Frequent Words in Paper Titles")
plt.xlabel("Frequency")
plt.ylabel("Word")
plt.tight_layout()
plt.show()

# 4. Distribution of paper counts by source_x
source_counts = df_clean["source_x"].value_counts()
print("Distribution by Source:\n", source_counts)

plt.figure(figsize=(8,5))
source_counts.plot(kind="bar")
plt.title("Publications by Source")
plt.xlabel("Source")
plt.ylabel("Number of Publications")
plt.tight_layout()
plt.show()

print("Analysis complete.")