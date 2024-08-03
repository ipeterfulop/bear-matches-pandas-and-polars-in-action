"""
Read the movies data from a JSON file into a Pandas DataFrame, 
write it to a Parquet file, and read it back into a DataFrame,
comparing the original and the read DataFrame.
"""

import os
import sys
import pandas as pd


data_provider_path = os.path.abspath(
    os.path.join(os.getcwd(), "../../../../", "data_providers")
)
sys.path.insert(0, data_provider_path)

from movie_data_provider import MovieDataProviderForPandas

# Load the movies data from a JSON file into a Pandas DataFrame
df_movies = MovieDataProviderForPandas.load_json_as_dataframe(
    json_file_name="movies.json",
    schema_provider=MovieDataProviderForPandas.get_movies_schema,
    index_column=None,
)

parquet_file_path = os.path.abspath(
    os.path.join(data_provider_path, "../data", "movies,parquet")
)

# Write the DataFrame to a Parquet file
# documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html
df_movies.to_parquet(parquet_file_path, engine="pyarrow", index=False)

# Read the Parquet file back into a DataFrame
df_movies_from_parquet = pd.read_parquet(parquet_file_path, engine="pyarrow")

print("Result of comparing the original DataFrame with the one read from the Parquet file:",
       df_movies.equals(df_movies_from_parquet))

