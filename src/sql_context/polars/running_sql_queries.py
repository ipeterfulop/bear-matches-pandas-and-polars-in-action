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

df_movie_genre = pl.read_parquet(movie_genre_parquet_file_path)

sql_context = pl.SQLContext()
sql_context.register("movies", df_movies)
sql_context.register("movie_genre", df_movie_genre)

df_movies_with_no_genre = sql_context.execute(
    """
    SELECT 
        m.movie_id, m.title, m.release_date
    FROM
        movies m
    LEFT JOIN movie_genre mg ON m.movie_id = mg.movie_id
    WHERE
        mg.genre_id IS NULL
    ORDER BY
        m.release_date    
    """).collect()
print(df_movies_with_no_genre)