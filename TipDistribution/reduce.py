#!/usr/bin/python
import sys

this_tip = None
cnt = 0

for line in sys.stdin:

    try:
        tip, _ = line.split('\t')
        tip = int(tip)
    except ValueError:
        continue

    if this_tip == tip:
        cnt += 1
    else:
        if this_tip != None:
            print ("%d,%d" % (this_tip, cnt))
        this_tip = tip
        cnt = 1

print ("%d,%d" % (this_tip, cnt))
