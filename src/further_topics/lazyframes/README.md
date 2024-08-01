# What is a LazyFrame?

A LazyFrame in Polars is a concept that defers computation on a DataFrame until necessary. Instead of executing operations immediately, LazyFrames build a computation graph representing the series of operations. This approach optimizes performance by executing all operations in a single, efficient step when required. This deferred execution allows for more efficient and optimized data processing.

## Resources 

* `[official documentation]` [Polars LazyFrame](https://docs.pola.rs/api/python/stable/reference/lazyframe/index.html) - This page gives an overview of all public LazyFrame methods.
* `[article]` [LazyFrame: Exploring Laziness in Dataframes from Polars in Python](https://medium.com/@HeCanThink/lazyframe-exploring-laziness-in-dataframes-from-polars-in-python-46da61d48e79)  Introduction to LazyFrame in Polars. A comprehensive guide to LazyFrame in Python. LazyFrame vs DataFrame. Polars LazyFrame vs Pandas DataFrame. Performance comparison of DataFrame vs LazyFrame.