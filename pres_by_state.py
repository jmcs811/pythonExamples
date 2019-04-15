#!/usr/bin/env python
state_list = {}

with open('/Users/jcasey/Downloads/presidents.txt') as PRES:
    for line in PRES:
        splitLine = line.split(':')
        state = splitLine[6]
        if state in state_list:
            state_list[state] += 1
        else:
            state_list[state] = 1

for key, value in sorted(state_list.items()):
    print(f'{key:30s} {value}')