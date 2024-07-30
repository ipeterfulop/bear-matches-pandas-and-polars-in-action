import os
import json
import inspect
import pandas as pd
import polars as pl
from typing import List, Dict, Tuple, Optional, Callable
from abc import ABC, abstractmethod


class MovieDataProvider(ABC):

    @staticmethod
    @abstractmethod
    def load_json_as_dataframe(json_file_name: str,
                               schema_provider: Callable,
                               index_column: Optional[str] = None):
        pass

    @staticmethod
    @abstractmethod
    def get_schema_aligned_dataframe(dataframe, schema):
        pass

    @staticmethod
    @abstractmethod
    def get_genres_schema():
        pass

    @staticmethod
    @abstractmethod
    def get_movies_schema():
        pass

    @staticmethod
    @abstractmethod
    def get_movie_genre_schema():
        pass


class MovieDataProviderForPandas(MovieDataProvider):

    @staticmethod
    def load_json_as_dataframe(json_file_name: str,
                               schema_provider: Callable,
                               index_column: Optional[str] = None) -> pd.DataFrame:

        path_to_json_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            json_file_name)

        try:
            with open(path_to_json_file, 'r') as file:
                json_data = json.load(file)

            df = pd.DataFrame(json_data)
            df.reset_index(drop=True, inplace=True)

            df = MovieDataProviderForPandas.get_schema_aligned_dataframe(df, schema_provider())

            if index_column:
                df.set_index(index_column, inplace=True)

        except ValueError as e:
            raise ValueError(f"\n [Error] Error generated while processing "
                             + f"{path_to_json_file} in {MovieDataProviderForPandas.__name__}."
                             + inspect.currentframe().f_code.co_name + f".\n Message:\n{e}")

        return df

    @staticmethod
    def get_schema_aligned_dataframe(dataframe: pd.DataFrame, schema: Dict) -> pd.DataFrame:

        for column, dtype in schema.items():
            if column in dataframe.columns:
                dataframe[column] = dataframe[column].astype(dtype)
            else:
                raise Exception(f"Warning: Column {column} not found in DataFrame")

        return dataframe

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
            "release_date": "object",
            "revenue": "int64",
            "runtime": "int64",
            "movie_status": "object",
            "tagline": "object",
            "vote_average": "float64",
            "vote_count": "int64"
        }

    @staticmethod
    def get_movie_genre_schema() -> Dict:
        return {
            "movie_id": "int64",
            "genre_id": "int64"
        }


class MovieDataProviderForPolars(MovieDataProvider):
    @staticmethod
    def load_json_as_dataframe(json_file_name: str, schema_provider: Callable, index_column: Optional[str] = None):
        pass

    @staticmethod
    def get_schema_aligned_dataframe(dataframe, schema):
        pass

    @staticmethod
    def get_genres_schema():
        pass

    @staticmethod
    def get_movies_schema():
        pass

    @staticmethod
    def get_movie_genre_schema():
        pass
