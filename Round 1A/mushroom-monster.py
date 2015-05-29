# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 1A - Problem A. Mushroom Monster
# https://code.google.com/codejam/contest/4224486/dashboard#s=p0
#
# Time:  O(N)
# Space: O(1)
#

for case in xrange(input()):
	n = input()
	m = map(int, raw_input().strip().split())
	first = sum(max(0, m[i]-m[i+1]) for i in xrange(n-1))
	rate = max(max(0, m[i]-m[i+1]) for i in xrange(n-1))
	second = sum(min(rate, m[i]) for i in xrange(n-1))
	print "Case #%d: %s %s" % (case+1, first, second)
