# Creating plugins for Polars

Yes, you can write plugins for Polars!  
[Marco Gorelli](https://www.linkedin.com/in/marcogorelli/) has created 
a [Polars plugin tutorial](https://marcogorelli.github.io/polars-plugins-tutorial/).  

See the 2 paragraphs below copied from Marco's tutorial:

## Why?

_Polars is an incredible and groundbreaking Dataframe library, and its expressions API is simply amazing. Sometimes, however, you need to express really custom business logic which just isn't in scope for the Polars API. In that situation, people tend to use map_elements, which lets you express anything but also kills most of Polars' benefits.  
But it doesn't have to be that way - with just **basic Rust knowledge and this tutorial**, I postulate that you'll be able to address at least 99% of inefficient map_elements tasks!_

## What will you learn (from Marco's tutorial)?

* _Writing simple single-column elementwise expressions_
* _Writing complex multi-column non-elementwise expressions which use third-party Rust packages_
* _How to share your plugin superpowers with others_