#!/usr/bin/env python

import sys
import re

sys.stdin.readline()

r = re.compile('\d+')

for l in sys.stdin.readlines():
  n = r.findall(l)
  print "CountryCode=%s,LocalAreaCode=%s,Number=%s" % tuple(n)
