#!/share/apps/python/2.7.10/gnu/bin/python
#-*- coding: utf-8 -*-

import sys
from datetime import datetime


for line in sys.stdin:

    l = line.strip().split(',')

    if len(l) == 18:
        total_revenue = float(l[-3]) + float(l[-5]) + float(l[-6])
        tip_amount = float(l[-3])
        if total_revenue > 0:
            tip_percent = tip_amount / total_revenue * 100

            print("%s\t%s,%s,%.2f" % (l[-9], total_revenue, tip_amount, tip_percent))
