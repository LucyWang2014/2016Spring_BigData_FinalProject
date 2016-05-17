#!/share/apps/python/2.7.10/gnu/bin/python
#-*- coding: utf-8 -*-
# Converting all the latitude and longtitude into zip iD

from __future__ import print_function

import sys
#sys.path.append('/home/jz1672/lib/python2.7/site-packages')
from operator import add

from pyspark import SparkContext

import sys
import traceback
import pickle as pkl

ids = pkl.load(open('id.pkl'))


def get_lat_long(ln):
    return (','.join(ln[:9]), (float(ln[9]), float(ln[10])), (float(ln[11]), float(ln[12])), ','.join(ln[13:]))


def convert_to_id(tup):
    diff = map(lambda x: (x[0]-tup[0])**2+(x[1]-tup[1])**2, ids)
    diff[0] = 10e5
    mindiff = reduce(lambda x,y: x if x[1]<y[1] else y, enumerate(diff))
    imin = mindiff[0]
    return str(imin)


def process(x):
    try:
        x = x.strip().split(',')
        lat_long = get_lat_long(x)
        new_str = ','.join([lat_long[0], convert_to_id(lat_long[1]), convert_to_id(lat_long[2]), lat_long[3]])
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
