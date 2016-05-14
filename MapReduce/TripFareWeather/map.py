#!/usr/bin/python

'''
columns:
medallion, hack_license, vendor_id, pickup_datetime, rate_code, store_and_fwd_flag, 
dropoff_datetime, passenger_count, trip_time_in_secs, 
trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, 
payment_type fare_amount surcharge mta_tax tip_amount tolls_amount total_amount
'''

import sys
import re
from datetime import datetime
 
for line in sys.stdin:

    line = line.strip().split(',')
    
    if len(line) == 21:

        
        dateindex = line[3].split()[0]

        print ('%s|tripfare\t%s' % (dateindex,','.join(line)))

    elif len(line) == 30: # weather
    
        date = re.sub('/','-',str(line[0])) if len(line[0]) > 0 else '1900-01-01' #date format yyyy-mm-dd
        tavg = line[2] if len(line[2]) > 0 else '' #average temperature in F
        snow = line[25] if len(line[23]) > 0 else ''#snowed
        rain = line[26] if len(line[24]) > 0 else ''#rained
        prcp = line[19] if len(line[19]) > 0 else ''#preciptation
        weekday = line[24] if len(line[24]) > 0 else ''
        season = line[23] if len(line[23]) > 0 else ''
         
        print ('%s|weather\t%s,%s,%s,%s,%s,%s' % (date,tavg,snow,rain,prcp,weekday,season))
            

