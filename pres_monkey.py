#!/usr/bin/env python
 
class President():
    def __init__(self, first, last, party):
        self.first = first
        self.last = last
        self.party = party
 
    def first_name(self):
        print('{}'.format(self.first))
 

def fullname(self):
    print('{} {}'.format(self.first, self.last))
 
pres = President('george', 'wash', 'demo')

# adding a method to a class
setattr(President, "first_name", fullname)
 
pres.first_name()