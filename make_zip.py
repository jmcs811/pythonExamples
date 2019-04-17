#!/usr/bin/env python
 
from zipfile import ZipFile, ZIP_DEFLATED
import os.path
 
# make a zip file consisting
# of the file listed below
wzip = ZipFile("chap8.zip", mode='w', compression=ZIP_DEFLATED)
for base in "save_potus_info.py read_potus_info.py pres_list.pic".split():
    wzip.write(base)