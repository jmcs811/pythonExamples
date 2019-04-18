#!/usr/bin/env python
 
import multiprocessing as mp
import datetime
import dateutil.parser
poolsize = 10
 
def date_to_obj(date_str: str):
    return dateutil.parser.parse(date_str)
 
# take to date objects
def date_subtract(line):
    birth_date = line[0]
    pres_date = line[1]
    age = (pres_date - birth_date).days / 365.2425
    return round(age, 2)
 
pool = mp.Pool(poolsize)
 
# list of tuples consisting of
# birth date and innaguration date
# this will give age at inauguration
# converted to date obj
list_of_names = [(date_to_obj(line[3]), date_to_obj(line[7])) for line in (line.split(':') for line in open('./DATA/presidents.txt'))]
 
# create new list holding the
# ages of the pres at inauguration
age_list = pool.map(date_subtract, list_of_names)
 
for i in age_list:
    print(i)