#!/usr/bin/env python
 
from collections import namedtuple
import pickle

# create named tuple
pres = namedtuple('pres', 'first last city state party')
pres_list = []

# add named tuple to a list
with open('./DATA/presidents.txt') as file:
    for line in file:
        splitLine = line.rstrip().split(':')
        p = pres(splitLine[2], splitLine[1], splitLine[5], splitLine[6], splitLine[9])
        pres_list.append(p)
 
# use pickle module to serialize
# the data
pickle.dump(pres_list, open("pres_list.pic", "wb"))