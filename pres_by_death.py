#!/usr/bin/env python
list_of_pres = []

with open('/Users/jcasey/Downloads/presidents.txt') as PRES:
    for line in PRES:
        splitLine = line.split(':')
        last_name = splitLine[1]
        first_name = splitLine[2]
        date_birth = splitLine[3]
        date_death = splitLine[4]
        pol_party = splitLine[9]
        list_of_pres.append((first_name, last_name, date_birth, date_death, pol_party))

# sorting list of tuples using lambda. tup[3] = date of death
list_of_pres = sorted(list_of_pres, key=lambda tup:tup[3])

for i in list_of_pres:
    print(f'First:{i[0]} LAST:{i[1]} DOB:{i[2]} DOD:{i[3]} PARTY:{i[4]}')