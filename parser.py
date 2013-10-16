#!/usr/bin/python
# coding: utf-8

import requests
import re

URL = 'https://news.ycombinator.com/item?id=6550469'


r = requests.get(URL)
results = re.findall('\d+ points',r.text)

print results