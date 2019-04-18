#!/usr/bin/env python
from typing import List
import multimethod
 
class Seed: pass
class Pig: pass
 
def grep(x: str) -> str:
    while True:
        coll = yield
        if x in coll:
            yield x
 
def sed (pattern: str, replacement: str) -> str:
    while True:
        value = yield
        if pattern in value:
            yield replacement
 
@multimethod
def sow(location, obj: Seed):
    print("this is a seed")
 
@multimethod
def sow(location, obj: Pig):
    print("this is a pig")
 
def append_42(x :List[int]):
    x.append(42)
    return x
 
if __name__ == '__main__':
    sow('test', Seed())
    sow('test', Pig())
    newlist = [32]
    append_42(newlist)
    print(newlist)