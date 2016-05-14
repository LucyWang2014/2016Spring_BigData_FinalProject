#!/usr/bin/python
import sys

trip_fares = []
weather = ""

for line in sys.stdin:
    
    date_tag, values = line.strip().split('\t', 1)
    date, tag = date_tag.strip().split('|', 1)

    if tag == 'tripsfare': 
        trip_fares.append(values)
    elif tag == 'weather': 
        weather = values
    
for tripfare in trip_fares:

    print ("%s\t%s" % (date,tripfare + ',' + weather))
    