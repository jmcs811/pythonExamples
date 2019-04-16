#!/usr/bin/env python
 
#list comprehension
# read in data from file
# store as tuple in list
list_of_names = [(line[2], line[1]) for line in (line.split(':') for line in open('./DATA/presidents.txt'))]
 
 # use list comprehension 
 # to store upper forms of
 # names
list_of_names_joined = [(name[0]+ ' ' + name[1]).upper() for name in list_of_names]
 
for name in list_of_names_joined:
    print(name)
