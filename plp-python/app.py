 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#  Load dataset (replace 'metadata.csv' path)
df = pd.read_csv('metadata.csv')

# Basic exploration
st.write("Data shape:", df.shape)
st.write(df.head())
st.write(df.info())
st.write("Missing values per column:\n", df.isnull().sum())

# Data Cleaning
# Drop columns with too many missing values (threshold example: 50%)
df_clean = df.dropna(thresh=len(df)*0.5, axis=1)

# Fill missing publication dates with a placeholder or drop rows
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
df_clean = df_clean.dropna(subset=['publish_time'])

# Extract publication year
df_clean['year'] = df_clean['publish_time'].dt.year

# Create abstract word count column
df_clean['abstract_word_count'] = df_clean['abstract'].fillna("").apply(lambda x: len(x.split()))

# Analysis
# Count papers by year
papers_per_year = df_clean['year'].value_counts().sort_index()

# Top journals by paper count
top_journals = df_clean['journal'].value_counts().head(10)

# Visualizations with matplotlib/seaborn
fig, ax = plt.subplots()
sns.barplot(x=papers_per_year.index, y=papers_per_year.values, ax=ax)
plt.xticks(rotation=45)
plt.title('Number of Publications per Year')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
st.pyplot(fig)

fig2, ax2 = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax2)
plt.title('Top 10 Journals by Number of Papers')
plt.xlabel('Number of Papers')
plt.ylabel('Journal')
st.pyplot(fig2)

# Streamlit basic app layout and interactivity
st.title('CORD-19 Research Papers Explorer')
st.write('Interactive dashboard for basic analysis of COVID-19 research metadata.')

year_range = st.slider('Select publication year range', int(papers_per_year.index.min()), int(papers_per_year.index.max()), (2019, 2022))
filtered_df = df_clean[(df_clean['year'] >= year_range[0]) & (df_clean['year'] <= year_range[1])]

st.write(f"Displaying {len(filtered_df)} papers published between {year_range[0]} and {year_range[1]}")
st.dataframe(filtered_df[['title', 'publish_time', 'journal', 'authors', 'abstract_word_count']].head(10))
