#!/usr/bin/python
import sys

trip_fares = []
this_date = None
weather = None

for line in sys.stdin:
    try:
        
        date_tag, values = line.strip().split('\t',1)
        date, tag = date_tag.strip().split('|',1)

        if date != this_date and len(trip_fares) > 0 and weather != None:
            for tripfare in trip_fares:
                print ("%s|%s" % (date,tripfare + ',' + weather))
            trip_fares = []
            weather = None

        if tag == 'tripfare': 
            trip_fares.append(values)
        elif tag == 'weather': 
            weather = values

        this_date = date

    except:
        pass

for tripfare in trip_fares:
    try:

        print ("%s|%s" % (date,tripfare + ',' + weather))

    except:

        pass