#!/usr/bin/env python

import sys
input = sys.stdin.read()
original_list = input.split()

slist = []
nlist = []

for thing in original_list:
  try:
    n = int(thing)
    nlist.append(thing)
  except:
    slist.append(thing)
    
slist.sort()
nlist.sort()
print "slist = %s" % slist
print "nlist = %s" % nlist

new_list = []
for thing in original_list:
  try:
    n = int(thing)
    new_list.append(nlist.pop(0))
  except:
    new_list.append(slist.pop(0))

print " ".join(new_list)
