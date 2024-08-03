"""
Read the movies data from a JSON file into a Polars DataFrame, 
write it to a Parquet file, and read it back into a DataFrame,
comparing the original and the read DataFrame.
"""
import os
import sys
import polars as pl

data_provider_path = os.path.abspath(
    os.path.join(os.getcwd(), "../../../../", "data_providers")
)
sys.path.insert(0, data_provider_path)

from movie_data_provider import MovieDataProviderForPolars 

# Load the movies data from a JSON file into a Polars DataFrame
df_movies = MovieDataProviderForPolars.load_json_as_dataframe(
    json_file_name="movies.json",
    schema_provider=MovieDataProviderForPolars.get_movies_schema,
    index_column=None,
)

parquet_file_path = os.path.abspath(
    os.path.join(data_provider_path, "../data", "movies.parquet")
)

# Write the DataFrame to a Parquet file
# documentation: https://docs.pola.rs/api/python/stable/reference/api/polars.DataFrame.write_parquet.html
df_movies.write_parquet(parquet_file_path,
                        compression="zstd",
                        use_pyarrow=True)

# Read the Parquet file back into a DataFrame
df_movies_from_parquet = pl.read_parquet(parquet_file_path)

# Compare the original DataFrame with the one read from the Parquet file
are_equal = df_movies.equals(df_movies_from_parquet)

print("Result of comparing the original DataFrame with the one read from the Parquet file:",
      are_equal)
