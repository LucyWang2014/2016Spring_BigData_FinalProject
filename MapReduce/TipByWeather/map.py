#!/usr/bin/python
import sys
import csv
import StringIO
 
for line in sys.stdin:
    
    key, values = line.strip().split('\t')  
    values = values.strip().split(',')  
    
    if values[22] == 1 & values[23] == 1:
        condition = 'snow-rain'
    elif values[22] == 1:
        condition = 'snow'
    elif values[23] == 1:
        condition = 'rain'
    elif values[22] == 0 & values[23] == 0:
        condition = 'clear'

    fare_amount = float(values[15])
    surcharge = float(values[16])
    tip_amount = float(values[18])

    revenue = fare_amount + surcharge + tip_amount
    if revenue > 0:
        tip_percent = tip_amount * 100.0 / revenue
    else:
        tip_percent = 0.0

    print ('%s\t%s,%s,%s,%s') % (condition, 1, revenue, tip_amount, tip_percent)
   







