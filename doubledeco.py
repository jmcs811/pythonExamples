#!/usr/bin/env python
from functools import wraps
 
# decorator that will 
# double the value 
# returned by the method
def doubler(old_func):
    def new_func(*args):
        res = old_func(*args)
        return res * 2
    return new_func
 
#using the decorator
@doubler
def addition(x):
    return x
 
a = addition(1)
print(a)