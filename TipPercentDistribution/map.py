#!/share/apps/python/2.7.10/gnu/bin/python
#-*- coding: utf-8 -*-

import sys
from datetime import datetime

from math import floor


for line in sys.stdin:

    l = line.strip().split(',')

    if len(l) == 18:
        total_revenue = float(l[-3]) + float(l[-5]) + float(l[-6])
        tip_amount = float(l[-3])

        if total_revenue > 0:
            tip_percent = tip_amount / total_revenue * 100

            if tip_percent < 10:
                tip_percent_group = 10
            elif tip_percent < 20:
                tip_percent_group = 20
            elif tip_percent < 30:
                tip_percent_group = 30
            else:
                tip_percent_group = 100


            print("%d" %  (tip_percent_group))
