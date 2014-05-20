#!/usr/bin/env python

import sys

terms = 0
list_of_nums = []

for line in sys.stdin:
    print "line = %s" % line
    if terms == 0:
        terms = int(line)
        continue
    list_of_nums = line.split()    

print "terms = %i, list = %s" % (terms, list_of_nums)
original_diff = int(list_of_nums[1]) - int(list_of_nums[0]) 
diff = 0

for n in range(2,len(list_of_nums)):
    diff = int(list_of_nums[n+1]) - int(list_of_nums[n]) 
    print "diff = %i, original = %i" % (diff, original_diff)
    if diff == original_diff:
        original_diff = diff
        continue
    else:
        missing = int(list_of_nums[n]) + original_diff
        break
        
print "%i was missing.  %i was the original_diff, %i was the bad diff" % (missing, original_diff, diff)
