#!/usr/bin/python

import requests
import urllib2
import urllib
import os

from sys import argv
from BeautifulSoup import BeautifulSoup

page = argv[1]
directory = argv[2]
html = BeautifulSoup(urllib2.urlopen(page))
html_images = html.findAll('img')
name = 1

for image in html_images:
    image_string = image.prettify()
    if 'http' and 'jpg' in image_string:
        image_url = image_string[image_string.index('http'):image_string.index('jpg')+3]
        urllib.urlretrieve(image_url, '{}/{}/{}'.format(os.getcwd(), directory, name))
        name += 1

