# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 1A - Problem C. Loggin
# https://code.google.com/codejam/contest/4224486/dashboard#s=p2
#
# Time:  O(N^2)
# Space: O(N)
#

from math import pi
from math import atan2

for c in xrange(input()):
    N = int(raw_input())
    dims = []
    for t in xrange(N):
    	dims.append(map(int, raw_input().strip().split()))

    print "Case #{}:".format(c+1)
    for i, p in enumerate(dims):
    	angles = [atan2(r[1]-p[1], r[0]-p[0]) for j, r in enumerate(dims) if j != i]
    	angles.extend([a + 2*pi for a in angles])
    	angles.sort()

    	min_remove = N - 1
        start, end = 0, 0
    	for i in xrange(len(angles) / 2):
            while start + 1 < len(angles) and \
                  angles[start] - angles[i]  < 1e-15:
                start += 1
    		while end < len(angles) and \
                  angles[end] - angles[i]  < pi - 1e-15:
    			end += 1
    		min_remove = min(min_remove, end - start)

    	print min_remove
