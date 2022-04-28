# peu
Python experiment utils

Utilities for software experimentation in python.
Here I publish small utilities I recurrently use in experimental projects.
This is also a pretext to publish my first package on PyPi.

This is a work in progress, and by now only includes a single
meaningful function: `peu.core:dict_product` perfroming the a
dictiionary flavoured cartesian product, useful to generate parameter
combination for software experiments.

# Example
```python
from peu.core import dict_product

params = {'a': [1,2,3],
          'b': {True, False}}

fixed = {'max_epochs':100,
         'scoring': 'accuracy'}

configs = dict_product (params, fixed=fixed)

# =>
# [{'a': 1, 'b': False, 'max_epochs': 100, 'scoring': 'accuracy'},
#  {'a': 1, 'b': True, 'max_epochs': 100, 'scoring': 'accuracy'},
#  {'a': 2, 'b': False, 'max_epochs': 100, 'scoring': 'accuracy'},
#  {'a': 2, 'b': True, 'max_epochs': 100, 'scoring': 'accuracy'},
#  {'a': 3, 'b': False, 'max_epochs': 100, 'scoring': 'accuracy'},
#  {'a': 3, 'b': True, 'max_epochs': 100, 'scoring': 'accuracy'}]



```


# Installation

The package is published on pypi @ https://pypi.org/project/peu-bandoos/0.0.1/

`$ pip install peu-bandoos==0.0.1`
