#!/usr/bin/env python
 
from operator import add
from functools import reduce
 
 # add all float values using reduce and map
 # lambda function converts str to float.
 # using the add operator
result = reduce(add, list(map(float, open('./DATA/float_values.txt'))))
 
print(f'{result:.2f}')