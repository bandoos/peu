from peu.core import dict_product
from pprint import pprint

params = {'a': [1, 2, 3], 'b': {True, False}}

fixed = {'max_epochs': 100, 'scoring': 'accuracy'}

configs = dict_product(params, fixed=fixed)

pprint(configs)
