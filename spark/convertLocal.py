#!/share/apps/python/2.7.10/gnu/bin/python
#-*- coding: utf-8 -*-
# Converting all the latitude and longtitude into zip iD

from __future__ import print_function

import sys
#sys.path.append('/home/jz1672/lib/python2.7/site-packages')
from operator import add

from geopy.geocoders import Nominatim
import sys
import traceback
g_locator = Nominatim()

def get_lat_long(ln):
    return (','.join(ln[:9]), (ln[10], ln[9]), (ln[12], ln[11]), ','.join(ln[13:]))


def convert_to_zip(tup):
    location = g_locator.reverse(tup[0] + ", " + tup[1])
    zip = location.address.split(',')[-2]
    return zip


def process(x):
    try:
        x = x.strip().split(',')
        lat_long = get_lat_long(x)
        new_str = ','.join([lat_long[0], convert_to_zip(lat_long[1]), convert_to_zip(lat_long[2]), lat_long[3]])
        return new_str
    except:
        #return ''
        pass


if __name__ == "__main__":
    file = open(sys.argv[1])
    newfile = open('1', 'w')
    cnt = 0
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        convert_line = process(line)
        newfile.write(convert_line + '\n')
        if cnt % 1000 == 0:
            print(cnt)
        cnt += 1
    newfile.close()

