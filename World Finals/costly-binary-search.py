# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 World Finals - Problem A. Costly Binary Search
# https://code.google.com/codejam/contest/5224486/dashboard#s=p0
#
# Time:  O(NlogN), pass in PyPy2 within 5 minutes (TLE for Python2), and C++ within 2 minutes
# Space: O(N)
#

# 1 <= N <= 10^6
MAX_N = 10 ** 6

# O(log2(N) * max(cost)) ~= 20 * 9 = 180
MAX_TIMES = 180

# left[t][p]: the farest position left to p which forms the range
#             [left[t][p], p) we can cover in time up to t
left = [[0 for _ in xrange(MAX_N + 1)] for _ in xrange(10)]

# right[t][p]: the farest position right to p which forms the range
#              [p, right[t][p]) we can cover in time up to t
right = [[0 for _ in xrange(MAX_N + 1)] for _ in xrange(10)]

def costly_binary_search():
    S = raw_input().strip()
    n = len(S)
    for p in xrange(n + 1):
        left[0][p] = p
        right[0][p] = p

    # Given t time, check if there is a point where
    # we'll be able to produce the entire array.
    for t in xrange(1, MAX_TIMES + 1):
        for p in xrange(n + 1):
            left[t % 10][p] = left[(t - 1) % 10][p]
            right[t % 10][p] = right[(t - 1) % 10][p]
        for p in xrange(n):
            tt = t - int(S[p])
            if tt >= 0:
                l = left[tt % 10][p]
                r = right[tt % 10][p + 1]
                # --(t-S[p])--   --(t-S[p])--
                # [l          ]p[           r]
                left[t % 10][r] = min(left[t % 10][r], l)
                right[t % 10][l] = max(right[t % 10][l], r)

        for p in reversed(xrange(1, n + 1)):
            # ------------t------------
            #       ------t------
            # ---------t---------
            # [lp   [l(p-1)      ](p-1)]p
            left[t % 10][p - 1] = min(left[t % 10][p - 1], left[t % 10][p])
        for p in xrange(n):
            # -------t-------------
            #   -----t----
            #   ----------t--------
            # [p[(p+1)    ][rp     ]]r(p+1)
            right[t % 10][p + 1] = max(right[t % 10][p + 1], right[t % 10][p])

        if right[t % 10][0] == n:
            # Found the min time which covers the entire array.
            return t

    return MAX_TIMES


for case in xrange(input()):
    print "Case #%d: %d" % (case+1, costly_binary_search())
