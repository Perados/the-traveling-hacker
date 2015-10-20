#!/usr/bin/env python

import requests
from sys import argv

original_css_file_path = argv[1]
original_css_file = open(original_css_file_path)
original_css_text = original_css_file.read() 

minified_css_text = requests.post('http://cssminifier.com/raw', {'input': original_css_text}).content

splitted = original_css_file_path.split('.')
minified_css_file_path = splitted[0] + '.min.' +splitted[1] 
minified_css_file = open(minified_css_file_path, 'wb')
minified_css_file.write(minified_css_text)
minified_css_file.close()

