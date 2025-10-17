import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('Netflix Dataset.csv')  # Update the filename if needed

# Data cleaning
df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')
df['Year'] = df['Release_Date'].dt.year
df.dropna(subset=['Year'], inplace=True)

# Movies vs TV Shows over time
content_trend = df.groupby(['Year', 'Category']).size().unstack()
content_trend.plot(kind='line', marker='o')
plt.title('Movies vs TV Shows Over Years')
plt.xlabel('Year')
plt.ylabel('Count')
plt.legend(title='Category')
plt.tight_layout()
plt.show()

# Genre/Type distribution (assuming 'Type' is genre)
top_genres = (
    df['Type']
    .value_counts()
    .head(10)
)
sns.barplot(y=top_genres.index, x=top_genres.values)
plt.title('Top 10 Genres on Netflix')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.tight_layout()
plt.show()

# Country-wise content evolution
top_countries = (
    df['Country']
    .value_counts()
    .head(10)
    .index.tolist()
)
country_trend = (
    df[df['Country'].isin(top_countries)]
    .groupby(['Year', 'Country'])
    .size()
    .unstack()
    .fillna(0)
)
country_trend.plot(kind='line', marker='o', figsize=(10, 6))
plt.title('Top Countries’ Content Contribution Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.legend(title='Country')
plt.tight_layout()
plt.show()

# Rating distribution by category
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Rating', hue='Category', order=df['Rating'].value_counts().index)
plt.title('Content Rating Distribution by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
