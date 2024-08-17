# Copy-on-write

Copy on Write is a mechanism to simplify the indexing API and improve performance through avoiding copies if possible. CoW means that any DataFrame or Series derived from another in any way always behaves as a copy.  

## Resources

* [`documentation`] [Copy on write](https://pandas.pydata.org/docs/dev/development/copy_on_write.html) and [Copy-on-Write (CoW)](https://pandas.pydata.org/docs/dev/user_guide/copy_on_write.html#copy-on-write)

* [`article`] [Deep Dive into pandas Copy-on-Write Mode: Part I](https://towardsdatascience.com/deep-dive-into-pandas-copy-on-write-mode-part-i-26982e7408c6)
