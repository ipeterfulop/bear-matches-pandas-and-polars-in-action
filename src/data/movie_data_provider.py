import os
import json
import inspect
import pandas as pd
from typing import List, Dict, Tuple

class MovieDataProvider:

    @staticmethod
    def get_genres_as_pandas_dataframe(json_file_name:str,
                                       validate_by_schema:bool=True) -> pd.DataFrame:
        path_to_json_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            json_file_name)
        
        try:
            df = pd.read_json(path_to_json_file)
        except ValueError as e:
            print(f"\n File not found {path_to_json_file} in {cls.__name__}:" 
                  + inspect.currentframe().f_code.co_name + f"\n {e}")
            exit(1)

        if validate_by_schema:

    @staticmethod
    def validate_by_schema(dataframe: pd.DataFrame, schema: Dict) -> bool:
        return True            





    @staticmethod
    def get_genre_schema_as_dict()->Dict:
        return {
            "genre_id": "int",
            "genre_name": "string"
            }