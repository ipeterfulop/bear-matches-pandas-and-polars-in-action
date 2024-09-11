# Compatibility

This section of the repository addresses the **compatibility aspects** of dataframe libraries. It includes examples of code libraries that provide solutions to compatibility issues.

## Narwhals

Narwhals is an extremely **lightweight and extensible compatibility** layer between dataframe libraries.  

* **Full API support:** cuDF, Modin, pandas, Polars, PyArrow  
* **Interchange-level support:** Ibis, Vaex, anything else which implements the DataFrame Interchange Protocol  
* **Typing:** Narwhals comes fully statically typed ([see more](https://narwhals-dev.github.io/narwhals/api-reference/typing/)).
* **Documentation**: [https://narwhals-dev.github.io/narwhals/](https://narwhals-dev.github.io/narwhals/)  
* **Source:** [https://github.com/narwhals-dev/narwhals](https://github.com/narwhals-dev/narwhals)

## Examples

*   The [`preserving_native_object.py`](preserving_native_object.py) example demonstrates how to apply the same manipulations (calculations) to both 
      pandas and Polars DataFrames using the Narwhals library while preserving the DataFrame annotations.

## Resources