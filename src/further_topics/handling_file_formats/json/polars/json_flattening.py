# Task:
# Given the JSON data below with nested structures, transform the content into a tabular format
# using Python's Polars library.
# This involves:
# - Extracting and normalizing nested fields into separate columns.
# - Handling nested lists by expanding them into multiple rows.
# - Ensuring the final DataFrame has a clear structure with all necessary columns and renamed headers for clarity.

import polars as pl
from typing import Dict

# Input data
data = [
    (
        "101",
        {
            "first_name": "George",
            "last_name": "Washington",
            "age": 57,
            "address": {
                "country_ISO2_code": "IR",
                "street": "Flowers road",
                "house_number": 38,
                "city": "Dublin",
            },
            "emails": [
                {"type": "work", "email": "georgew@workplace.com"},
                {"type": "personal", "email": "georgew@gmail.com"}
            ]
        },
    ),
    (
        "102",
        {
            "first_name": "John",
            "last_name": "Adams",
            "age": 61,
            "address": {
                "country_ISO2_code": "US",
                "street": "Main street",
                "house_number": 12,
                "city": "New York",
            },
            "emails": [
                {"type": "personal", "email": "john.adams@gmail.com"}
            ]
        },
    ),
    (
        "103",
        {
            "first_name": "Thomas",
            "last_name": "Jefferson",
            "age": 83,
            "address": {
                "country_ISO2_code": "US",
                "street": "Broadway",
                "house_number": 4,
                "city": "Chicago",
            },
            "emails": [
                {"type": "work", "email": "thomas.jefferson@thefirm.com"},
                {"type": "personal", "email": "thomas@thejeffersos.com"}
            ]
        },
    ),
]


def flatten_info(id: int, info: Dict) -> Dict:
    """
    Flattens nested fields within a dictionary.

    This function extracts and flattens nested fields from the input dictionary,
    creating a new dictionary with a simplified structure to prepare JSON data for tabular representation.

    :param id:
        The id of the record.

    :type id: int

    :param info:
        Dictionary containing nested user information. The expected structure includes
        'first_name', 'last_name', 'age', and 'address' which itself contains
        'country_ISO2_code', 'street', 'house_number', and 'city'.

    :type info: Dict

    :return:
        A flattened dictionary with the following keys:
        - 'first_name': User's first name.
        - 'last_name': User's last name.
        - 'age': User's age.
        - 'country_ISO2_code': Country ISO2 code from the address.
        - 'street': Street name from the address.
        - 'house_number': House number from the address.
        - 'city': City from the address.

    :rtype: Dict
    """
    flattened = {
        "id": id,
        "first_name": info["first_name"],
        "last_name": info["last_name"],
        "age": info["age"],
        "country_ISO2_code": info["address"]["country_ISO2_code"],
        "street": info["address"]["street"],
        "house_number": info["address"]["house_number"],
        "city": info["address"]["city"],
    }
    return flattened


# Convert the data to a Polars DataFrame
df = pl.DataFrame(data, schema=[("id", pl.Utf8), ("info", pl.Object)])

# Flatten the info column
flattened_data = [flatten_info(row["id"], row["info"]) for row in df.to_dicts()]
emails_data = [(row["id"], email["type"], email["email"]) for row in df.to_dicts() for email in row["info"]["emails"]]

# Create Polars DataFrames
flattened_df = pl.DataFrame(flattened_data)
emails_df = pl.DataFrame(emails_data, schema=[("id", pl.Utf8), ("email_type", pl.String), ("email_address", pl.String)])

# Join the data
final_df = flattened_df.join(emails_df, on="id")

# Show the final DataFrame
print(final_df)
