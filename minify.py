#!/usr/bin/env python

import requests
from sys import argv

original_file_path = argv[1]
file_type = argv[2]
original_file = open(original_file_path)
original_text = original_file.read()
minifier = 'cssminifier' if file_type == 'css' else 'javascript-minifier'

minified_text = requests.post('http://' + minifier + '.com/raw', {'input': original_text}).content

splitted = original_file_path.split('.')
minified_file_path = splitted[0] + '.min.' +splitted[1]
minified_file = open(minified_file_path, 'wb')
minified_file.write(minified_text)
minified_file.close()

