#!/usr/bin/env python

from president import President

p = President(44)

print(f'President {p.first_name} {p.last_name}, the {p.term_number}th president, was born in {p.birth_city} {p.birth_state}')