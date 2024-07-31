"""
A list of movies is available in a JSON file. Additionally, a list of genres and movie-genre pairs
are also provided as JSON files.
Write a Python script reads the data into a Polars DataFrames with appropriate schemas
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
import polars as pl

data_provider_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', 'data_providers'))
sys.path.insert(0, data_provider_path)
from movie_data_provider import MovieDataProviderForPolars

df_movies = (
    MovieDataProviderForPolars.load_json_as_dataframe(json_file_name="movies.json",
                                                      schema_provider=MovieDataProviderForPolars.get_movies_schema,
                                                      index_column="movie_id"))

df_movie_genre = (
    MovieDataProviderForPolars.load_json_as_dataframe(json_file_name="movie_genre.json",
                                                      schema_provider=MovieDataProviderForPolars.get_movie_genre_schema))

df_genres = (
    MovieDataProviderForPolars.load_json_as_dataframe(json_file_name="genres.json",
                                                      schema_provider=MovieDataProviderForPolars.get_genres_schema))

# Merge dataframes to combine movies with their respective genres
df_combined = (df_movies
.join(df_movie_genre, on='movie_id', how="inner").join(df_genres, on='genre_id')
.select([
    pl.col('movie_id'),
    pl.col('title'),
    pl.col('genre_name')
]))

# Aggregate genres for each movie
df_aggregated = df_combined.group_by('movie_id', 'title').agg(genres_list=pl.col("genre_name"))
print(df_aggregated.dtypes)

# if you want to have the genres as a concatenated string instead of a list see manipulation below
df_aggregated = df_aggregated.with_columns(genres_concatenated=pl.col("genres_list").list.join(", "))
print(df_aggregated)
