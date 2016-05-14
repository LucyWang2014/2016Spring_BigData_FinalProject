#!/usr/bin/python
import sys

current_key = None
trip = False
fare = False

for line in sys.stdin:
    
    key_tag, values = line.strip().split('\t', 1)
    key, tag = key_tag.strip().split('|', 1)

    if key != current_key:    
        if trip and fare:
            print ("%s,%s" % (current_key, trip + ',' + fare))
            trip = False
            fare = False
    
    if tag == 'trip': # trip
        trip = values
    elif tag == 'fare': # fare
        fare = values
    
    current_key = key