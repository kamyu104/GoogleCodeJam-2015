# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Qualification Round - Problem B. Infinite House of Pancakes
# https://code.google.com/codejam/contest/6224486/dashboard#s=p1
#
# Time:  O(max(P) * D)
# Space: O(1)
#

def pancake():
    D = int(input())
    P = map(int, raw_input().strip().split())
    time = max(P)
    
    # Try to split each plate into target count of pancakes, and count waiting time
    for cnt in xrange(2, max(P)):
        wait = 0
        for cakes in P:
            wait += (cakes-1)//cnt
        time = min(time, cnt+wait)
    return time

for case in xrange(input()):
    print 'Case #%d: %d' % (case+1, pancake())
