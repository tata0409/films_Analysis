import pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

url = "movies_metadata.csv"
movies_df = pd.read_csv(url)

#print(movies_df.head())
movies_df.info()

#print(movies_df.describe())


def extract_genres(genres_str):
    try:
        genres = ast.literal_eval(genres_str)
        return [genre['name'] for genre in genres]
    except (ValueError, TypeError):
        return []


movies_df['genres'] = movies_df['genres'].apply(extract_genres)
movies_df['budget'] = pd.to_numeric(movies_df['budget'], errors='coerce')
movies_df['popularity'] = pd.to_numeric(movies_df['popularity'], errors='coerce')
movies_df['revenue'] = pd.to_numeric(movies_df['revenue'], errors='coerce')
movies_df['budget'] /= 1000000
movies_df['revenue'] /= 1000000
movies_df.dropna(subset=['budget', 'revenue'], inplace=True)
movies_df['release_year'] = pd.to_datetime(movies_df['release_date'], errors='coerce').dt.year
print(movies_df['release_year'])
print(movies_df['original_language'])

genre_exploded = movies_df[['title', 'release_year', 'budget', 'revenue', 'genres', 'popularity']].explode('genres')
print(genre_exploded['budget'])
genre_count = genre_exploded['genres'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=genre_count.index, y=genre_count.values)
plt.title("Number of films by genre")
plt.xlabel("Genre")
plt.ylabel("Number")
plt.xticks(rotation=45)
plt.tight_layout()

plt.figure(figsize=(10, 6))
sns.barplot(x=movies_df['budget'], y=movies_df['revenue'])
plt.title("Budget vs Revenue")
plt.xlabel("Budget in millions")
plt.ylabel("Revenue in millions")
plt.xticks(rotation=90)
plt.tight_layout()

plt.figure(figsize=(10, 6))
sns.barplot(x=movies_df['release_year'], y=movies_df['popularity'])
plt.title("Popularity trend")
plt.xlabel("Release year")
plt.ylabel("Popularity")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
