#!/usr/bin/env python

import sys
import re

r = re.compile('[A-Z]{5}[0-9]{4}[A-Z]')
lines = [line.rstrip() for line in sys.stdin.readlines()[1:]]

for pan in lines:
  if r.match(pan):
    print "YES"
  else:
    print "NO"
