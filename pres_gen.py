#!/usr/bin/env python

# Generator function. Is iterable
def presidentGen(file_name):
    with open(file_name) as PRES:
        for line in PRES:
            splitLine = line.split(':')
            yield str(splitLine[2] + ' ' + splitLine[1]).upper()

for president in presidentGen('/Users/jcasey/Downloads/presidents.txt'):
    print(president)