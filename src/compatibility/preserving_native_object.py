import numpy as np
import pandas as pd
import polars as pl
import narwhals as nw
from narwhals.typing import IntoFrameT


def create_dataframe_from_calculation(df_native: IntoFrameT, target_column: str) -> IntoFrameT:
    """
    Create a new DataFrame from the input DataFrame by calculating the sum, mean, and standard deviation
    of the specified column.

    It returns a new DataFrame with the calculated values preserving the native object "type"/annotation.

    :param df_native: The input DataFrame in native format.
    :type df_native: IntoFrameT
    :param target_column: The name of the column for which to calculate sum, mean, and standard deviation.
    :type target_column: str
    :return: A new DataFrame with the calculated values.
    :rtype: IntoFrameT
    """
    df = nw.from_native(df_native)
    df = df.select(
        a_sum=nw.col(target_column).sum(),
        a_mean=nw.col(target_column).mean(),
        a_std=nw.col(target_column).std(),
    )
    return nw.to_native(df)


if __name__ == "__main__":
    np.random.seed(42)
    random_data_a = np.random.rand(100)
    random_data_b = np.random.rand(100)

    df_observation_pd = pd.DataFrame({
        'observations_a': random_data_a,
        'observations_b': random_data_b
    })

    df_result_pd = create_dataframe_from_calculation(df_observation_pd, "observations_a")
    print(type(df_result_pd))
    print(df_result_pd)

    df_observation_pl = pl.DataFrame({
        "observations_a": random_data_a,
        "observations_b": random_data_b
    })

    df_result_pl = create_dataframe_from_calculation(df_observation_pl, "observations_a")
    print(type(df_result_pl))
    print(df_result_pl)
