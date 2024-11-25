"""
This module provides a framework for loading and processing movie data into structured formats using
Pandas or Polars DataFrames.
It defines an abstract base class MovieDataProvider with implementations for both libraries.
"""

import os
import json
import inspect
import pandas as pd
import polars as pl
from typing import List, Dict, Tuple, Optional, Callable, Any, Union
from abc import ABC, abstractmethod


class MovieDataProvider(ABC):
    """
       Abstract Base Class for providing movie data functionality.

       This class defines the interface for loading and processing movie-related data
       and requires concrete implementations for methods to handle various data operations.
    """

    @staticmethod
    @abstractmethod
    def load_json_as_dataframe(json_file_name: str,
                               schema_provider: Callable,
                               index_column: Optional[str] = None) -> Union[pd.DataFrame | pl.DataFrame]:
        """
            Abstract method to load a JSON file and convert it into a DataFrame.

            :param json_file_name: The name of the JSON file to load.
            :param schema_provider: A callable that provides the schema for the DataFrame.
            :param index_column: Optional column to set as the index for the DataFrame.
            :return: A DataFrame of either Pandas or Polars type.
        """
        pass

    @staticmethod
    @abstractmethod
    def get_schema_aligned_dataframe(dataframe, schema) -> Union[pd.DataFrame | pl.DataFrame]:
        """
        Aligns the schema of a given DataFrame.

        Args:
            dataframe (Union[pd.DataFrame, pl.DataFrame]): The input DataFrame to align.
            schema (Dict): A dictionary defining the expected schema where keys are column names
                and values are target data types.

        Returns:
            Union[pd.DataFrame, pl.DataFrame]: A schema-aligned DataFrame.
        """
        pass

    @staticmethod
    @abstractmethod
    def get_genres_schema() -> Dict[str, Any]:
        pass

    @staticmethod
    @abstractmethod
    def get_movies_schema() -> Dict[str, Any]:
        pass

    @staticmethod
    @abstractmethod
    def get_movie_genre_schema() -> Dict[str, Any]:
        pass


class MovieDataProviderForPandas(MovieDataProvider):
    """
        Concrete implementation of `MovieDataProvider` using the Pandas library.

        This class provides methods to load JSON data into Pandas DataFrames, align them with schemas,
        and retrieve predefined schemas for genres, movies, and movie-genre relationships.

        Methods:
            - load_json_as_dataframe: Load a JSON file into a Pandas DataFrame.
            - get_schema_aligned_dataframe: Align a DataFrame with a given schema.
            - get_genres_schema: Retrieve the schema for genres.
            - get_movies_schema: Retrieve the schema for movies.
            - get_movie_genre_schema: Retrieve the schema for movie-genre relationships.

        Examples:
            Load a movies dataset and align it to a predefined schema:

            >>> schema_provider = MovieDataProviderForPandas.get_movies_schema
            >>> df = MovieDataProviderForPandas.load_json_as_dataframe("movies.json", schema_provider)
            >>> print(df.head())
    """

    @staticmethod
    def load_json_as_dataframe(json_file_name: str,
                               schema_provider: Callable,
                               index_column: Optional[str] = None) -> pd.DataFrame:
        """
        Load a JSON file into a Pandas DataFrame and align it with a provided schema.

        Args:
            json_file_name (str): Name of the JSON file to be loaded (located in the `data` directory).
            schema_provider (Callable): Function that returns a schema dictionary for column alignment.
            index_column (Optional[str]): Column name to set as the index in the resulting DataFrame. Defaults to None.

        Returns:
            pd.DataFrame: The loaded and schema-aligned Pandas DataFrame.

        Raises:
            ValueError: If there is an issue reading or processing the JSON file.

        Examples:
            Load and align a JSON file of movies:

            >>> schema_provider = MovieDataProviderForPandas.get_movies_schema
            >>> df = MovieDataProviderForPandas.load_json_as_dataframe("movies.json", schema_provider)
            >>> print(df.info())

            Load and set an index column:

            >>> df = MovieDataProviderForPandas.load_json_as_dataframe(
            ...     "movies.json",
            ...     MovieDataProviderForPandas.get_movies_schema,
            ...     index_column="movie_id"
            ... )
            >>> print(df.index)
        """
        
        path_to_json_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '..',
            'data',
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
    def get_genres_schema() -> Dict[str, Any]:
        return {
            "genre_id": "int64",
            "genre_name": "object"
        }

    @staticmethod
    def get_movies_schema() -> Dict[str, Any]:
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
    def get_movie_genre_schema() -> Dict[str, Any]:
        return {
            "movie_id": "int64",
            "genre_id": "int64"
        }


class MovieDataProviderForPolars:

    @staticmethod
    def load_json_as_dataframe(json_file_name: str,
                               schema_provider: Callable,
                               index_column: Optional[str] = None) -> pl.DataFrame:
        path_to_json_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '..',
            'data',
            json_file_name)

        try:
            with open(path_to_json_file, 'r') as file:
                json_data = json.load(file)

            df = pl.DataFrame(json_data)
            df = MovieDataProviderForPolars.get_schema_aligned_dataframe(df, schema_provider())

        except ValueError as e:
            raise ValueError(f"\n [Error] Error generated while processing "
                             + f"{path_to_json_file} in {MovieDataProviderForPolars.__name__}."
                             + inspect.currentframe().f_code.co_name + f".\n Message:\n{e}")

        return df

    @staticmethod
    def get_schema_aligned_dataframe(dataframe: pl.DataFrame, schema: Dict) -> pl.DataFrame:
        """
        Aligns the schema of a Polars DataFrame to match a schema provided as argument.

        This method ensures that the columns of the input DataFrame are cast to the specified types
        defined in the provided schema. If a column in the schema is not found in the DataFrame, an
        exception is raised.

        :param dataframe:
            The input Polars DataFrame that needs schema alignment.

        :type dataframe:
            pl.DataFrame

        :param schema:
            A dictionary defining the expected schema where the keys are column names and the values
            are the target data types.

        :type schema:
            dict

        :return:
            A Polars DataFrame
        """
        for column, dtype in schema.items():
            if column in dataframe.columns:
                dataframe = dataframe.with_columns(pl.col(column).cast(dtype))
            else:
                raise Exception(f"Warning: Column {column} not found in DataFrame")

        return dataframe

    @staticmethod
    def get_genres_schema() -> Dict[str, Any]:
        return {
            "genre_id": pl.Int64,
            "genre_name": pl.Utf8
        }

    @staticmethod
    def get_movies_schema() -> Dict[str, Any]:
        return {
            "movie_id": pl.Int64,
            "title": pl.Utf8,
            "budget": pl.Int64,
            "homepage": pl.Utf8,
            "overview": pl.Utf8,
            "popularity": pl.Float64,
            "release_date": pl.Utf8,
            "revenue": pl.Int64,
            "runtime": pl.Int64,
            "movie_status": pl.Utf8,
            "tagline": pl.Utf8,
            "vote_average": pl.Float64,
            "vote_count": pl.Int64
        }

    @staticmethod
    def get_movie_genre_schema() -> Dict[str, Any]:
        return {
            "movie_id": pl.Int64,
            "genre_id": pl.Int64
        }
