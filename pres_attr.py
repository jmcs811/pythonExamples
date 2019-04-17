#!/usr/bin/env python
 
class President():
    def __init__(self, first, last, party):
        self.first = first
        self.last = last
        self.party = party
 
pres = President("Jorge", "Washingtino", "no part")
 
# access the field using getattr
# instead of pres.first
print(f'{getattr(pres, "first")}')