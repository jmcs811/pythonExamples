#!/usr/bin/env python
import pickle
from collections import namedtuple

# named tuple must be recreated exactly
# in order to be deserialized
pres = namedtuple('pres', 'first last city state part')

# use pickle module to read
# in serialized file
pres = pickle.load(open('./pres_list.pic', 'rb'))

print(pres)