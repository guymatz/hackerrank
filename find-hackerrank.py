#!/usr/bin/env python

import sys

lines = [ line.rstrip() for line in sys.stdin.readlines()[1:] ]

for l in lines:
  if l.startswith('hackerrank') and l.endswith('hackerrank'):
    print "0"
    continue
  if l.startswith('hackerrank'):
    print "1"
    continue
  elif l.endswith('hackerrank'):
    print "2"
    continue
  else:
    print "-1"
