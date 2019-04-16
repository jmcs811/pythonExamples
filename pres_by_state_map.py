#!/usr/bin/env python
from itertools import groupby 

# use map and lambda to split line
# on 6th field. The values get added
# to the list
result = list(map(lambda x: x.split(':')[6:7], open('./DATA/presidents.txt')))

# use group by to show
# number of presidents 
# from which state
count = groupby(result, key=lambda x: x)

for a in count:
    print(a)