#!/usr/bin/python
import sys

this_pickup_location = None
this_tip = 0
this_revenue = 0
this_tip_percent = 0
cnt = 0

for line in sys.stdin:

    pickup_location, content = line.strip().split("\t", 1)
    revenue, tip, tip_percent = content.split(",")

    try:
        revenue = float(revenue)
        tip = float(tip)
        tip_percent = float(tip_percent)
    except ValueError:
        continue

    if pickup_location == this_pickup_location:
        this_revenue += revenue
        this_tip += tip
        this_tip_percent += tip_percent
        cnt += 1
    else:
        if this_pickup_location:
            print ("%s,%.2f,%.2f,%.2f" % (this_pickup_location, this_revenue,
                                                this_tip, this_tip_percent/cnt))
        this_pickup_location = pickup_location
        this_tip = tip
        this_revenue = revenue
        this_tip_percent = tip_percent
        cnt = 1

print ("%s,%.2f,%.2f,%.2f" % (this_pickup_location, this_revenue, this_tip, this_tip_percent/cnt))
