# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 World Finals - Problem C. Pretty Good Proportion
# https:#code.google.com/codejam/contest/5224486/dashboard#s=p2
#
# Time:  O(NlogN)
# Space: O(N)
#

PRECISION = 1000000

# Find the minimum of |dy/dx - f|
def check(F, sum, i, j, min_y, min_x, ans):
    dy, dx = abs(sum[j] - sum[i]), abs(j - i)
    # y / x = |dy/dx - f|
    y, x = abs(dy * PRECISION - dx * F), dx * PRECISION
    if y * min_x < x * min_y:
        min_y, min_x, ans = y, x, min(i, j)
    elif y * min_x == x * min_y and min(i, j) < ans:
        # If they are the same slope,
        # update ans to the smallest i.
        ans = min(i, j)
    return min_y, min_x, ans


def pretty_good_proportion():
    N, f = raw_input().strip().split()
    N, f = int(N), float(f)
    F = int(f * PRECISION)
    s = raw_input().strip()

    sum = [0] * (N + 1)
    for i in xrange(N):
        sum[i + 1] = sum[i] + 1 if s[i] == '1' else sum[i]

    p = []
    for i in xrange(N+1):
        # Diff error f(i): #(1s) - i * f
        p.append((sum[i]*PRECISION - i*F, i))

    # Time: O(nlogn)
    # Sort the pair (f(i), i) by diff error f(i)
    p.sort()

    # ans is with the min diff error |dy / dx - f| = min_y / min_x
    min_y, min_x, ans = 1, 1, N - 1

    # Try out all neighboring pairs which could form
    # the substring with the minima f(i) difference "dy".
    # Find the min diff error |dy / dx - f|
    # in all neighboring pairs.
    for i in xrange(N):
        min_y, min_x, ans = check(F, sum, p[i][1], p[i + 1][1], \
                                  min_y, min_x, ans)
    return ans


for case in xrange(input()):
    # Read the input.
    print "Case #%d: %d" % (case+1, pretty_good_proportion())

