#!/usr/bin/python

'''
columns:
medallion, hack_license, vendor_id, pickup_datetime, rate_code, store_and_fwd_flag, 
dropoff_datetime, passenger_count, trip_time_in_secs, 
trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, 
payment_type, fare_amount, surcharge, mta_tax, tip_amount, tolls_amount, total_amount,
tavg, snow, rain, prcp, weekday, season
'''

import sys
import csv
import StringIO
 
for line in sys.stdin:
    
    key, values = line.strip().split('|')  
    values = values.strip().split(',')  
    '''
    if values[22] == 1 & values[23] == 1:
        condition = 'snow-rain'
    elif values[22] == 1:
        condition = 'snow'
    elif values[23] == 1:
        condition = 'rain'
    elif values[22] == 0 & values[23] == 0:
        condition = 'clear'
    '''
    
    payment_type = values[14]
    passenger_count = values[7]
    fare_amount = float(values[15])
    surcharge = float(values[16])
    tip_amount = float(values[18])
    weekday = values[25]
    season = values[26]
    snow = values[22]
    rain = values[23]
    tavg = values[21]


    revenue = fare_amount + surcharge + tip_amount
    if revenue > 0:
        tip_percent = tip_amount * 100.0 / revenue
    else:
        tip_percent = 0.0

    print ('%s|%s|%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s') % (key, payment_type, passenger_count, 1, revenue, tip_amount, tip_percent,
        weekday, season, snow, rain, tavg)
   







