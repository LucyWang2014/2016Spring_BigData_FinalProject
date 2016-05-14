#!/usr/bin/python
import sys
 
for line in sys.stdin:

    line = line.strip().split(',')
    
    if len(line) == 11: # fare
        medallion = line[0]
        hack_license = line[1]
        vendor_id = line[2]
        pickup_datetime = line[3]
        payment_type = line[4]
        fare_amount = line[5]
        surcharge = line[6]
        mta_tax = line[7]
        tip_amount = line[8]
        tolls_amount = line[9]
        total_amount = line[10]
        
        print ('%s,%s,%s,%s|fare\t%s,%s,%s,%s,%s,%s,%s' % (medallion, hack_license, 
        	vendor_id, pickup_datetime, payment_type, fare_amount, surcharge, mta_tax, 
        	tip_amount, tolls_amount, total_amount))
    
    elif len(line) == 14: # trip
    	medallion = line[0]
    	hack_license = line[1]
    	vendor_id = line[2]
    	rate_code = line[3]
    	store_and_fwd_flag = line[4]
    	pickup_datetime = line[5]
    	dropoff_datetime = line[6]
    	passenger_count = line[7]
    	trip_time_in_secs = line[8]
    	trip_distance = line[9]
    	pickup_longitude = line[10]
    	pickup_latitude = line[11]
    	dropoff_longitude = line[12]
    	dropoff_latitude = line[13]
#         
        print ('%s,%s,%s,%s|trip\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (medallion, hack_license, vendor_id, 
        	pickup_datetime, rate_code, store_and_fwd_flag, dropoff_datetime, passenger_count, 
        	trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, 
        	dropoff_latitude))
