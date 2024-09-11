"""
Running SQL queries directly on Polars dataframes
"""
import os
import sys
import polars as pl

data_provider_path = os.path.abspath(
    os.path.join(os.getcwd(), "../../", "data_providers")
)
sys.path.insert(0, data_provider_path)

movies_parquet_file_path = os.path.abspath(
    os.path.join(data_provider_path, "../data", "movies.parquet")
)

df_movies = pl.read_parquet(movies_parquet_file_path)

movie_genre_parquet_file_path = os.path.abspath(
    os.path.join(data_provider_path, "../data", "movie_genre.parquet")
)

