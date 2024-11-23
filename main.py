import pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "movies_metadata.csv"
movies_df = pandas.read_csv(url)

print(movies_df.head())
movies_df.info()

print(movies_df.describe())

def extract_genres(genres_str):
    try:
        genres = ast
