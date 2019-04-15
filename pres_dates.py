#!/usr/bin/env python

# prompt for user input
name_query = input("Enter Last Name\n")

# Read data into dictionary
with open('/Users/jcasey/Downloads/presidents.txt') as PRES:
    for line in PRES:
        split_line = line.split(":")
        # if last name field equals the query
        # pull out the values and print them
        if split_line[1] == name_query:
            last_name = split_line[1]
            date_of_birth = split_line[3]
            date_of_death = split_line[4]
            if date_of_death == 'NONE':
                date_of_death = '* * *'
            print(f'{last_name:10s} {date_of_birth} {date_of_death}')

