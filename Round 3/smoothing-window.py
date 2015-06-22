# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 3 - Problem B. Smoothing Window
# https://code.google.com/codejam/contest/4254486/dashboard#s=p1
#
# Time:  O(N)
# Space: O(N)
#

def smoothing_window(N, K, S):
    # diff[i]: x[i + K] - x[i]
    diff = [S[i + 1] - S[i] for i in xrange(N - K)]
    P, Q = [], S[0]
    for i in xrange(K):
        cur_diff, min_diff, max_diff = 0, 0, 0
        for j in xrange(i, N - K, K):
            cur_diff += diff[j]
            min_diff = min(min_diff, cur_diff)
            max_diff = max(max_diff, cur_diff)
        P.append(max_diff - min_diff)
        Q += min_diff

    # P[i]: max(x[i + m * K]) - min(x[i + n * K]), for i in xrange (0, K).
    # Q:    sum(min(x[i + n * K])), for i in xrange(0, K).
    # Let max(x[i + m * K]) = [Q / K] + max(P), for i in xrange(0, K)
    # If sum([Q / K] + max(P) - P[i]) >= Q <=> max(P) * K - sum(P) >= Q % K, max_diff = max(P)
    # Else max_diff = max(P) + 1
    max_diff = 0
    if max(P) * K - sum(P) >= Q % K:
        max_diff = max(P)
    else:
        max_diff = max(P) + 1
    return max_diff

for case in xrange(input()):
    N, K = map(int, raw_input().strip().split())
    S = map(int, raw_input().strip().split())
    print "Case #%d: %d" % (case+1, smoothing_window(N, K, S))
