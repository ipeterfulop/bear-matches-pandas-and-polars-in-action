import os
import json
import inspect
import pandas as pd
from typing import List, Dict, Tuple, Optional, Callable


class MovieDataProvider:

    @staticmethod
    def load_json_as_pandas_dataframe(json_file_name: str,
                                      schema_provider: Callable,
                                      schema_validator: Callable,
                                      index_column: Optional[str] = None) -> pd.DataFrame:

        path_to_json_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            json_file_name)

        try:
            with open(path_to_json_file, 'r') as file:
                json_data = json.load(file)

            df = pd.DataFrame(json_data)
            df = MovieDataProvider.get_schema_aligned_dataframe(df, schema_provider())

            if index_column:
                df.set_index(index_column, inplace=True)

        except ValueError as e:
            print(f"\n [Error] Error generated while processing {path_to_json_file} in {MovieDataProvider.__name__}."
                  + inspect.currentframe().f_code.co_name + f".\n Message:\n{e}")
            exit(1)

        return schema_validator(df, schema_provider())

    @staticmethod
    def get_schema_aligned_dataframe(dataframe: pd.DataFrame, schema: Dict) -> pd.DataFrame:
        for column, dtype in schema.items():
            dataframe[column] = dataframe[column].astype(dtype)

        return df

    @staticmethod
    def get_genres_schema() -> Dict:
        return {
            "genre_id": "int64",
            "genre_name": "object"
        }

    @staticmethod
    def get_movies_schema() -> Dict:
        return {
            "movie_id": "int64",
            "title": "object",
            "budget": "int64",
            "homepage": "object",
            "overview": "object",
            "popularity": "float64",
            "release_date": "object",  # Use 'datetime64' if you want to convert it to datetime
            "revenue": "int64",
            "runtime": "int64",
            "movie_status": "object",
            "tagline": "object",
            "vote_average": "float64",
            "vote_count": "int64"
        }

    @staticmethod
    def get_movie_genres_schema() -> Dict:
        return {
            "movie_id": "int",
            "genre_id": "int"
        }
