#!/usr/bin/env python

class President:

    # constructor
    def __init__(self, number):
        self._get_data(number)

    # read in data from file, set the member vars accordingly
    # if none match i.e. > 45 || < 0 raise error
    def _get_data(self, number):
        with open('./DATA/presidents.txt') as data:
            for line in data:
                splitLine = line.split(':')
                if int(splitLine[0]) == int(number):
                    self._term_number = splitLine[0]
                    self._first_name = splitLine[2]
                    self._last_name = splitLine[1]
                    self._birth_date = splitLine[3]
                    self._death_date = splitLine[4]
                    self._birth_city = splitLine[5]
                    self._birth_state = splitLine[6]
                    self._term_start = splitLine[7]
                    self._term_end = splitLine[8]
                    self._party = splitLine[9]
                    break
            else:
                raise ValueError("Invalid input")
    
    # getters will return the member var value
    @property
    def term_number(self):
        return self._term_number
    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def birth_date(self):
        return self._birth_date

    @property
    def death_date(self):
        return self._death_date

    @property
    def birth_city(self):
        return self._birth_city

    @property
    def birth_state(self):
        return self._birth_state

    @property
    def term_start(self):
        return self._term_start

    @property
    def term_end(self):
        return self._term_end

    @property
    def party(self):
        return self._party