import os
import sys
import pandas as pd
import json

data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', 'data'))
sys.path.insert(0, data_path)
from movie_data_provider import MovieDataProvider

df_movies = MovieDataProvider.load_json_as_pandas_dataframe(json_file_name="movies.json",
                                                            schema_provider=MovieDataProvider.get_movies_schema,
                                                            schema_validator=MovieDataProvider.get_schema_aligned_dataframe,
                                                            index_column="movie_id")
