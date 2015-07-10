# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round C - Problem E. River Flow
# https://code.google.com/codejam/contest/4254486/dashboard#s=p4
#
# Time:  O(D^2 * logD)
# Space: O(D)
#

def possible(D, d):
    # Let xi be di - di-1 when i > 1, and x1 = d1 - d2D.
    # xi represents the difference in flow between day i and
    # the previous day in the 2D-day cycle.
    x = [d[i] - d[i-1] for i in xrange(len(d))]
    farmers = 0
    while D > 0:
        for i in xrange(D):
            if (x[i] + x[i + D]) % 2 == 1:
                return -1
            else:
                num = (x[i] - x[i + D]) / 2
                if num >= 0:
                    farmers += num
                    d = d[:i] + [flow - num for flow in d[i:i + D]] + d[i + D:2 * D]
                else:
                    farmers += -num
                    d = [flow + num for flow in d[:i]] + d[i:i + D] + [flow + num for flow in d[i + D:2 * D]]
                if min(d) < 0:
                    return -1
                x[i] = (x[i] + x[i + D]) / 2
        D >>= 1
    return farmers

def river_flow(N, D, d):
    # If the river flow data is not periodic with period 2D.
    # the farmers are cheating.
    if len([i for i in xrange(N-2*D) if d[i] != d[i+2*D]]):
        return "CHEATERS!"
    # Count farmers by first 2D river flow data.
    farmers = possible(D, d[:2*D])
    if farmers < 0:
        return "CHEATERS!"
    return farmers

for case in xrange(input()):
    # Read the input.
    N, D = map(int, raw_input().strip().split())
    d = map(int, raw_input().strip().split())

    print "Case #%d: %s" % (case+1, river_flow(N, D, d))

