# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round C - Problem E. River Flow
# https://code.google.com/codejam/contest/4254486/dashboard#s=p4
#
# Time:  O(DlogD)
# Space: O(D)
#

def possible(D, d):
    # Let xi be di - di-1 when i > 1, and x1 = d1 - d2D.
    # xi represents the difference in flow between day i and
    # the previous day in the 2D-day cycle.
    x = [d[i] - d[i - 1] for i in xrange(len(d))]
    farmers, P = 0, D
    # For each period P in D, D / 2, D / 4, ..., 1.
    while P > 0:
        # For each T in period P.
        for T in xrange(P):
            # x[T] + x[T+P] should be even.
            if (x[T] + x[T + P]) % 2 == 1:
                return -1
            elif x[T] - x[T + P] != 0:
                cnt = (x[T] - x[T + P]) / 2
                # Update flow data by removing F(T, P) quantity.
                if cnt > 0:
                    farmers += cnt
                    for flow in xrange(T, T + P):
                        flow -= cnt
                else:
                    farmers += -cnt
                    for flow in xrange(T):
                        flow -= -cnt
                    for flow in xrange(T + P, T + 2 * P):
                        flow -= -cnt
                # There should be no flow data less than zero.
                if min(d) < 0:
                    return -1
                # Update flow data difference after removing F(T, P) quantity.
                x[T] = (x[T] + x[T + P]) / 2
        P >>= 1
    return farmers

def river_flow(N, D, d):
    # If the river flow data is not periodic with period 2D.
    # the farmers are cheating.
    if len([i for i in xrange(N - 2*D) if d[i] != d[i + 2*D]]):
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

