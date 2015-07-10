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
    x = [d[i]-d[i-1] for i in xrange(len(d))]
    tot = 0
    while D > 0:
        for j in xrange(D):
            if (x[j] + x[j + D]) % 2 == 1:
                return -1
            else:
                scr = (x[j] - x[j + D]) / 2
                if x[j] >= x[j + D]:
                    tot += scr
                    d = d[:j] + [z - scr for z in d[j:j+D]] + d[j+D:2*D]
                else:
                    tot -= scr
                    d = [z+scr for z in d[:j]] + d[j:j+D] + [z+scr for z in d[j+D:2*D]]
                if min(d) < 0:
                    return -1
                x[j] = (x[j] + x[j + D]) / 2
        D >>= 1
    return tot

def river_flow(N, D, d):
    if len([i for i in xrange(N-2*D) if d[i] != d[i+2*D]]):
        return "CHEATERS!"
    tot = possible(D, d[:2*D])
    if tot < 0:
        return "CHEATERS!"
    return tot

for case in xrange(input()):
    # Read the input.
    N, D = map(int, raw_input().strip().split())
    d = map(int, raw_input().strip().split())

    print "Case #%d: %s" % (case+1, river_flow(N, D, d))

