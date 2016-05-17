#-*- coding: utf-8 -*-
# Converting all the latitude and longtitude into zip iD

from __future__ import print_function

import sys
#sys.path.append('/home/jz1672/lib/python2.7/site-packages')
from operator import add

from pyspark import SparkContext

from geopy.geocoders import Nominatim

import sys
import traceback

g_locator = Nominatim()


def get_lat_long(ln):
    return (','.join(ln[:9]), (ln[10], ln[9]), (ln[12], ln[11]), ','.join(ln[13:]))


def convert_to_zip(tup):
    location = g_locator.reverse(tup[0] + ", " + tup[1])
    zip = location.address.split(',')[-2]
    return zip.strip()


def process(x):
    try:
        x = x.strip().split(',')
        lat_long = get_lat_long(x)
        new_str = ','.join([lat_long[0], convert_to_zip(lat_long[1]), convert_to_zip(lat_long[2]), lat_long[3]])
        return new_str
    except:
        traceback.print_exc()
        pass


if __name__ == "__main__":
    sc = SparkContext(appName="test")
    data = sc.textFile(sys.argv[1])
    data_converted = data.map(lambda x: process(x))
    data_converted_collect = data_converted.collect()

    for line in data_converted_collect:
        print("%s" % (str(line)))

    sc.stop()
