#!/usr/bin/env python
last_names = []

with open('./Data/presidents.txt') as PRES:
    for line in PRES:
        splitLine = line.split(':')
        last_names.append(splitLine[1])

# list comprehension 
last_names = [name.upper() for name in last_names]

for name in last_names:
    print(name)