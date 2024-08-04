# Interacting with various file formats

## Covered file formats

### JSON

* JSON flattening and json data transformation into tabular format can be
  challenging. The examples in the `json_flattening.py` file demonstrate how to
  handle nested JSON data and flatten it into a tabular format using Pandas and Polars.  
  **Solution:** [Pandas](json/pandas/json_flattening.py) | [Polars](json/polars/json_flattening.py)

### Parquet

Parquet has become a de-facto standard for data storage today due to several key advantages:

- **Data compression**: By using various encoding and compression algorithms, Parquet files significantly reduce memory
  consumption.
- **Columnar storage**: This is crucial for analytic workloads where fast data read operations are essential. More
  details on this will be discussed later in the article.
- **Language agnostic**: As previously mentioned, developers can use different programming languages to manipulate data
  stored in Parquet files.
- **Open-source format**: This ensures you are not locked into a specific vendor.
- **Support for complex data types**: Parquet files can handle complex data structures efficiently.

* Reading and writing Parquet files is a common task in data processing. The examples in the repo file demonstrate how
  to read and write Parquet files using Pandas and Polars.  
  **Solution:** [Pandas](parquet/pandas/writing_reading_parquet.py) | [Polars](polars/pandas/writing_reading_parquet.py)

### Apache ORC

Optimized Row Columnar (ORC) is a column-oriented data storage format that belongs to the Apache Hadoop ecosystem.  
Although ORC files and their processing might not usually fall within a data scientist's typical responsibilities, there
are times when you'll need to extract and manipulate these files using your preferred data munging libraries.    

* Reading and writing OCR files 
  in [Pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_orc.html#pandas.read_orc) and Polars 
  is a common task in data processing. The examples in the repo file demonstrate how
  to read and write OCR files using Pandas and Polars.  
  **Solution:** [Pandas](orc/pandas/writing_reading_parquet.py) | Polars


## Resources

* `[article]` [Pandas Parquet and Feather - Tips, Tricks and Best Practices](https://python.plainenglish.io/pandas-parquet-and-feather-92636bb3555d) -
  _may require active Medium subscription to access the full article_.
    

