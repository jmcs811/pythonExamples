#!/usr/bin/env python
 
import sys, os
from collections import Counter
 
def printExtensions(path: str):
    list_of_files = [f.split('.')[1] for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
 
    counter = Counter()
    for ext in list_of_files:
        counter[ext] += 1
 
    for item, count in counter.items():
        print(f'{item} {count}')
 
printExtensions('/Users/jcasey/Downloads')