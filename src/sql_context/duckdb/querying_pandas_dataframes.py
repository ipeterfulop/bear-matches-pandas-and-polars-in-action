"""
This module contains a brief example of how to query a pandas DataFrame using DuckDB.
In certain cases, when you want to query a large pandas dataframe using SQL, 
or when you want to take advantage of DuckDB's query optimization and execution capabilities
you can use the DuckDB API to query the pandas DataFrame.

Task:
    Given a pandas DataFrame containing movie data, list the number of movies released each year
    where the number of movies released in a year is greater than 30. List the years in descending order
    of the number of movies released.

Docs: https://duckdb.org/docs/guides/python/sql_on_pandas.html
"""

import duckdb
import pandas as pd
import os
import sys


data_provider_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', 'data_providers'))
sys.path.insert(0, data_provider_path)
from movie_data_provider import MovieDataProviderForPandas

df_movies = (
    MovieDataProviderForPandas.load_json_as_dataframe(json_file_name="movies.json",
                                                      schema_provider=MovieDataProviderForPandas.get_movies_schema,
                                                      index_column=None))

df_movies['release_date'] = pd.to_datetime(df_movies['release_date'], format='%Y-%m-%d', errors='coerce')

query = """
        SELECT 
            YEAR(release_date), COUNT(*) as number_of_movies
        FROM 
            df_movies
        GROUP BY 
            YEAR(release_date)
        HAVING COUNT(*) > 30
        ORDER BY COUNT(*) DESC    
        """

df_movie_stats = duckdb.sql(query).df(index=False)
print(df_movie_stats)
