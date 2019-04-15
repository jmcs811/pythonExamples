#!/usr/bin/env python
list_of_pres = []

with open('/Users/jcasey/Downloads/presidents.txt') as PRES:
    for line in PRES:
        splitLine = line.split(':')