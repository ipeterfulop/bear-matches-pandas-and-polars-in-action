# Task:
# Given the JSON data below with nested structures, transform the content into a tabular format
# using Python's Pandas library.
# This involves:
# - Extracting and normalizing nested fields into separate columns.
# - Handling nested lists by expanding them into multiple rows.
# - Ensuring the final DataFrame has a clear structure with all necessary columns and renamed headers for clarity.

import pandas as pd

# input data
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

# Convert the data to a DataFrame
df = pd.DataFrame(data, columns=["id", "info"])

# Normalize the nested JSON data
info_df = pd.json_normalize(df["info"])

# Concatenate the original id column with the normalized info DataFrame
flattened_df = pd.concat([df["id"], info_df], axis=1)

# Explode the emails column
flattened_df = flattened_df.explode("emails")

# Normalize the emails column
emails_df = pd.json_normalize(flattened_df["emails"])

# Reset indexes to ensure uniqueness
flattened_df = flattened_df.reset_index(drop=True)
emails_df = emails_df.reset_index(drop=True)

# Concatenate the flattened DataFrame with the emails DataFrame
final_df = pd.concat([flattened_df.drop(columns=["emails"]), emails_df], axis=1)


# Concatenate the flattened DataFrame with the emails DataFrame
final_df = pd.concat([flattened_df.drop(columns=["emails"]), emails_df], axis=1)

# Rename columns for clarity
final_df.rename(columns={
    "emails.type": "email_type",
    "emails.email": "email_address",
    "address.country_ISO2_code": "country_ISO2_code",
    "address.street": "street",
    "address.house_number": "house_number",
    "address.city": "city"
}, inplace=True)

# Show the flattened DataFrame
print(final_df)

