# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round C - Problem C. Runaway Quail
# https://code.google.com/codejam/contest/4254486/dashboard#s=p2
#
# Time:  O(N^3)
# Space: O(N^2)
#

def representive_quails(quails):
    k = 0
    # Sort by position.
    quails = sorted(quails)
    # Simplify quails by strictly decreasing speed.
    for i in xrange(len(quails)):
        while k > 0 and quails[i][1] >= quails[k - 1][1]:
            k -= 1
        quails[k] = quails[i]
        k += 1
    # Only keep representive quails.
    return quails[:k]

def catch_time(Y, t, quail):
    return (t * quail[1] + quail[0]) / (Y - quail[1])

def runaway_quail(Y, N, P, S):
    left_quails, right_quails = [], []
    for i in xrange(N):
        if P[i] < 0:
            left_quails.append([-P[i], S[i]])
        else:
            right_quails.append([P[i], S[i]])
    left_quails = representive_quails(left_quails)
    right_quails = representive_quails(right_quails)
    time = [[float("inf") for j in xrange(len(right_quails) + 1)]\
              for i in xrange(len(left_quails) + 1)]
    time[0][0] = 0.0

    # Dynamic programming.
    min_time = float("inf")
    for i in xrange(len(left_quails) + 1):
        for j in xrange(len(right_quails) + 1):
            t, T = 0.0, time[i][j]
            for k in xrange(j, len(right_quails)):
                x = catch_time(Y, T, right_quails[k])
                t = max(t, catch_time(Y, T, right_quails[k]))
                # Update time to catch right_quails[k],
                # and goes back to position zero.
                # It costs 2t.
                time[i][k + 1] = min(time[i][k + 1], T + 2 * t)

            # No need to go back to position zero for the last one, it costs t.
            if i == len(left_quails):
                min_time = min(min_time, T + t)

            t = 0.0
            for k in xrange(i, len(left_quails)):
                x = catch_time(Y, T, left_quails[k])
                t = max(t, catch_time(Y, T, left_quails[k]))
                # Update time to catch left_quails[k],
                # and goes back to position zero.
                # It costs 2t.
                time[k + 1][j] = min(time[k + 1][j], T + 2 * t)

            # No need to go back to position zero for the last one, it costs t.
            if j == len(right_quails):
                min_time = min(min_time, T + t)

    return min_time

for case in xrange(input()):
    # Read the input.
    Y, N = map(int, raw_input().strip().split())
    P = map(int, raw_input().strip().split())
    S = map(int, raw_input().strip().split())

    print "Case #%d: %.15f" % (case+1, runaway_quail(Y, N, P, S))
