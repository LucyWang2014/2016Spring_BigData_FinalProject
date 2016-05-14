#!/share/apps/python/2.7.10/gnu/bin/python
#-*- coding: utf-8 -*-
# Converting all the latitude and longtitude into zip iD

from __future__ import print_function

import sys
#sys.path.append('/home/jz1672/lib/python2.7/site-packages')
from operator import add

from pyspark import SparkContext

import urllib
from lxml import html
from lxml.etree import tostring
import sys


def get_lat_long(ln):
    return (','.join(ln[:9]), (ln[10], ln[9]), (ln[12], ln[11]), ','.join(ln[13:]))


def get_url(lat, long):
    return 'http://www.melissadata.com/lookups/latlngzip4.asp?lat=' + \
        lat + '&lng=' + long


def get_html(url):
    return html.fromstring(urllib.urlopen(url).read())


def get_address_zip(pg):
    add = tostring(pg.xpath("/html/body/div[1]/table[4]/tr[4]/td/b/br[1]")[0])
    add = add[add.find('<br/>')+5:]
    zip = tostring(pg.xpath("/html/body/div[1]/table[4]/tr[4]/td/b/br[2]")[0])
    zip = zip[5: zip.find('&')]
    return add, zip


def convert_to_zip(tup):
    url = get_url(tup[0], tup[1])
    page = get_html(url)
    _,zip = get_address_zip(page)
    return zip


def process(x):
    try:  # TODO time out shit
        x = x.strip().split(',')
        lat_long = get_lat_long(x)
        new_str = ','.join([lat_long[0], convert_to_zip(lat_long[1]), convert_to_zip(lat_long[2]), lat_long[3]])
        return new_str
    except:
        return ''


if __name__ == "__main__":
    sc = SparkContext(appName="test")
    data = sc.textFile(sys.argv[1])
    data_converted = data.map(lambda x: process(x))
    data_converted_collect = data_converted.collect()

    for line in data_converted_collect:
        print("%s" % (str(line)))

    sc.stop()
