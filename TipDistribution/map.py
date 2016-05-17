#!/share/apps/python/2.7.10/gnu/bin/python
#-*- coding: utf-8 -*-

import sys
from datetime import datetime

from math import floor


for line in sys.stdin:

    l = line.strip().split(',')

    if len(l) == 20:
        tip_amount = floor(float((l[-3])))

        if tip_amount >= 0:

            print("%d\t%d" % (tip_amount, 1))
