#!/usr/bin/env python
state_list = {}

# read in data and add to dictionary
with open('./DATA/presidents.txt') as PRES:
    for line in PRES:
        splitLine = line.split(':')
        state = splitLine[6]
        if state in state_list:
            state_list[state] += 1
        else:
            state_list[state] = 1

# print the key-value pair
for key, value in sorted(state_list.items()):
    print(f'{key:30s} {value}')