"""
Read the movies data from a JSON file into a Pandas DataFrame,
write it to a ORC(Optimized Row Columnar) file, and read it back into a DataFrame,
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

orc_file_path = os.path.abspath(
    os.path.join(data_provider_path, "../data", "movies.orc")
)

# Write the DataFrame to an ORC file
df_movies.to_orc(orc_file_path, engine="pyarrow", index=False)

# Read the ORC file back into a DataFrame
df_movies_from_orc = pd.read_orc(orc_file_path)
# Check if schema is retained
print(df_movies_from_orc.dtypes)
# Compare the original DataFrame with the one read from the ORC file
print("Result of comparing the original DataFrame with the one read from the ORC file:",
      df_movies.equals(df_movies_from_orc))

