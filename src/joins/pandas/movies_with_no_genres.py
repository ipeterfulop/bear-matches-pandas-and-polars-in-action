"""
A list of movies released is available in a JSON file.
Additionally,  a list of genres and movie-genre pairs are also provided as JSON files.
Find the movies with no genres associated with them.
The detailed schema of the data can be found in the <repo root folder>/src/movie_data_provider.py file.
"""

import os
import sys
import pandas as pd

data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', 'data'))
sys.path.insert(0, data_path)
from movie_data_provider import MovieDataProviderForPandas

df_movies = (
    MovieDataProviderForPandas.load_json_as_dataframe(json_file_name="movies.json",
                                                      schema_provider=MovieDataProviderForPandas.get_movies_schema,
                                                      index_column="movie_id"))

df_movie_genre = (
    MovieDataProviderForPandas.load_json_as_dataframe(json_file_name="movie_genre.json",
                                                      schema_provider=MovieDataProviderForPandas.get_movie_genre_schema))

df_movies['release_date'] = pd.to_datetime(df_movies['release_date'], format="%Y-%m-%d").dt.date

# Solution 1:
# find movies with no genres associated with them like the movies that have a movie_id
# that is not in the movie_genre dataframe
df_movies_with_no_genres_1 = df_movies[~df_movies.index.isin(df_movie_genre['movie_id'])]

# Solution 2:
# Join the two dataframes and find the rows where the genre_id is missing
merged_df = df_movies.join(df_movie_genre.set_index('movie_id'), on='movie_id', how='left')
df_movies_with_no_genres_2 = merged_df[merged_df['genre_id'].isnull()]

print(f"Solution 1: shape {df_movies_with_no_genres_1.shape} {df_movies_with_no_genres_1}")
print(f"Solution 2: shape {df_movies_with_no_genres_2.shape} {df_movies_with_no_genres_2}")

same_movies_retrieved = set(df_movies_with_no_genres_1.index) == set(df_movies_with_no_genres_2.index)

# Output the result
print(f"Do the solutions retrieve the same movies? {same_movies_retrieved}")
