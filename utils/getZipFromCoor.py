#!/usr/bin/python

import urllib
from lxml import html
from lxml.etree import tostring
import sys


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


def main(argv):
    ''' Driver program for testing'''
    lat = argv[1]
    long = argv[2]
    url = get_url(lat, long)
    page = get_html(url)
    add, zip = get_address_zip(page)
    print(add, zip)


if __name__ == '__main__':
    main(sys.argv)
