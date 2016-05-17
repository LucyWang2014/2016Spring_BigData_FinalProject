#!/usr/bin/python

import sys
import collections

total_condition = collections.Counter()

for line in sys.stdin:
    
    day_payment_passCount, values = line.strip().split('\t', 1)
    day, payment_type, passenger_count = day_payment_passCount.strip().split('|',2)
    count, revenue, tip_amount, tip_percent, weekday, season, snow, rain, tavg = values.strip().split(',')

    count = int(count)
    revenue = float(revenue)
    tip_amount = float(tip_amount)
    tip_percent = float(tip_percent)

    condition = ','.join([day, payment_type, passenger_count])

    try:
        total_condition[condition][0] = total_condition[condition][0] + count
        total_condition[condition][1] = total_condition[condition][1] + revenue
        total_condition[condition][2] = total_condition[condition][2] + tip_amount
        total_condition[condition][3].append(tip_percent)
        total_condition[condition][4] = weekday
        total_condition[condition][5] = season
        total_condition[condition][6] = snow
        total_condition[condition][7] = rain
        total_condition[condition][8] = tavg
    except:
        total_condition[condition] = [count, revenue, tip_amount, [tip_percent], weekday, season, snow, rain, tavg]
        

for condition in total_condition.keys():
    total_count = total_condition[condition][0]
    total_rev = total_condition[condition][1]
    total_tip = total_condition[condition][2]
    weekday = total_condition[condition][4]
    season = total_condition[condition][5]
    snow = total_condition[condition][6]
    rain = total_condition[condition][7]
    tavg = total_condition[condition][8]

    if total_rev == 0:
        tip_percent = 0
        avg_tip_percent = 0
    else:
        tip_percent = total_tip / total_rev
        avg_tip_percent = sum(total_condition[condition][3]) * 1.0 / total_count

    print ("%s\t%s,%s,%.2f,%.2f,%s,%s,%s,%s,%s") % (condition, total_count, total_rev, tip_percent, avg_tip_percent, 
        weekday, season, snow, rain, tavg)
    
    