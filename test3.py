#!/usr/bin/env python

import sys

num_dcs = sys.stdin.readline()

dcs = []
min = 1
max = 1

for line in sys.stdin.readlines():
  line.strip()
  copies = line.split()
  copies = map(int, copies)
  copy_num = copies.pop(0)
  if copies[0] < min:
    min = copies[0]
  if copies[-1] > max:
    max = copies[-1]
  dcs.append(sorted(copies))

for n in range(0, len(dcs)):
  print "%i %s" % (n+1, dcs[n])

copy_exists_in = {}
for i in range(min, max+1):
  #print "i = %i" % i
  for dc in range(0, len(dcs)):
    #print "dc = %i" % dc
    #print "i = %i" % i
    if i in dcs[dc]:
      copy_exists_in[i] = dc
      break

for dc in range(0, len(dcs)):
  for i in range(min, max+1):
    #print "checking dc  = %i, i = %i" % (dc+1, i+1)
    if i not in dcs[dc]:
      print "%i %i %i" % (i, copy_exists_in[i]+1, dc+1)
