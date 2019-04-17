#!/usr/bin/env python
 
# print every other letter in
# the string
def every_other(self):
    return(self.name[::2])
 
def set_up(self, name):
    self.name = name
 
# create a class programtically
# add the methods above to the 
# class
SillyString = type("SillyString", (), {
    "name":"lame",
    "every_other": every_other,
    "__init__": set_up
    })
 
ss = SillyString('this is a testssssssssssssssssss')
print(ss.every_other())