#!/usr/bin/python
import sys
import collections

total_condition = collections.Counter()
for line in sys.stdin:
    
    condition, values = line.strip().split('\t', 1)
    count, revenue, tip_amount, tip_percent = values.strip().split(',')

    count = int(count)
    revenue = float(revenue)
    tip_amount = float(tip_amount)
    tip_percent = float(tip_percent)

    try:
        total_condition[condition][0] = total_condition[condition][0] + count
        total_condition[condition][1] = total_condition[condition][1] + revenue
        total_condition[condition][2] = total_condition[condition][2] + tip_amount
        total_condition[condition][3].append(tip_percent)
    except:
        total_condition[condition] = [count, revenue, tip_amount, [tip_percent]]
        

for condition in total_condition.keys():
    total_count = total_condition[condition][0]
    total_rev = total_condition[condition][1]
    total_tip = total_condition[condition][2]

    if total_rev == 0:
        tip_percent = 0
        avg_tip_percent = 0
    else:
        tip_percent = total_tip / total_rev
        avg_tip_percent = sum(total_condition[condition][3]) * 1.0 / total_count

    print ("%s\t%s,%s,%.2f,%.2f") % (condition, total_count, total_rev, tip_percent, avg_tip_percent)
    
    