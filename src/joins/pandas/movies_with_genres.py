"""
A list of movies is available in a JSON file. Additionally, a list of genres and movie-genre pairs
are also provided as JSON files.
Write a Python script reads the data into a Pandas DataFrames with appropriate schemas
and lists the movies in ascending order, specifying the list of genres. Each movie appears only once in the list.

Steps:
1. Read the JSON files into a Pandas DataFrames.
2. Perform joins to combine movies with their respective genres.
3. Aggregate the genres for each movie.
4. List the movies in ascending order with the associated genres. Make the genres available as a list of strings and
a concatenated string as well.
"""
import os
import sys
import pandas as pd

data_provider_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', 'data_providers'))
sys.path.insert(0, data_provider_path)
from movie_data_provider import MovieDataProviderForPandas

df_movies = (
    MovieDataProviderForPandas.load_json_as_dataframe(json_file_name="movies.json",
                                                      schema_provider=MovieDataProviderForPandas.get_movies_schema,
                                                      index_column="movie_id"))

df_movie_genre = (
    MovieDataProviderForPandas.load_json_as_dataframe(json_file_name="movie_genre.json",
                                                      schema_provider=MovieDataProviderForPandas.get_movie_genre_schema))

df_genres = (
    MovieDataProviderForPandas.load_json_as_dataframe(json_file_name="genres.json",
                                                      schema_provider=MovieDataProviderForPandas.get_genres_schema))

# Join dataframes to combine movies with their respective genres
df_combined = df_movies.join(df_movie_genre.set_index('movie_id'), on='movie_id', how="inner").join(
    df_genres.set_index('genre_id'), on='genre_id', how="inner")

# Aggregate the dataframe from the previous step.
# select the first title from each group and
# apply a lambda function to create a list of genre names from each group
df_aggregated = df_combined.groupby('movie_id').agg({
    'title': 'first',
    'genre_name': lambda x: list(x),
}).reset_index()

df_aggregated['genre_name'] = df_aggregated['genre_name'].apply(
    lambda genres: [str(genre) if not pd.isnull(genre) else '' for genre in genres]
)

# Concatenate genres into a single string
df_aggregated['genres_concatenated'] = df_aggregated['genre_name'].apply(lambda x: ', '.join(x))

print(df_aggregated)

# if you want to have the genres as a concatenated string instead of a list see manipulation below
# df_aggregated['genres_concatenated'] = df_aggregated['genre_name'].apply(lambda x: ', '.join(x))
# print(df_aggregated)
