#!/usr/bin/env  python
import sys

test_cases = map(int, sys.stdin.readlines())

for num in test_cases[1:]:
  pi = 0.0
  for n in range(0, num):
    pi += ((-1.0) ** n) / ((2.0*n)+1)
  print "%0.15f" % pi
