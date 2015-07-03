# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round C - Problem D. Log Set
# https://code.google.com/codejam/contest/4254486/dashboard#s=p3
#
# Time:  O(P^2 * logP)
# Space: O(P)
#

from math import log

def log_set(P, E, F):
    G = {E[i]-E[0]:F[i] for i in xrange(P)}
    v = []
    nums = [E[i]-E[0] for i in xrange(P-1, -1, -1)]
    goal = -E[0]
    G2 = dict(G)  # clone of  G.
    while len(G) > 1:
        Gk = sorted(G.keys())
        num = Gk[1]
        v.append(num)
        for i in Gk:
            if (i + num) in G:
                G[i + num] += -G[i]
            else:
                G[i + num] = -G[i]
        G = {a:b for (a,b) in G.items() if b != 0}
    v = [0] * int(log(G[0], 2)) + v
    w = []
    for num in v[::-1]:
        for i in sorted(G2.keys()):
            if (i + num) in G2:
                G2[i + num] += -G2[i]
            else:
                G2[i + num] = -G2[i]
        G2 = {a:b for (a,b) in G2.items() if b != 0}
        if goal - num in G2:
            w.append(-num)
            goal += -num
        else:
            w.append(num)
    w = sorted(w)
    return " ".join(str(i) for i in w)

for case in xrange(input()):
    # Read the input.
    P = input()
    E = map(int, raw_input().strip().split())
    F = map(int, raw_input().strip().split())

    print "Case #%d: %s" % (case+1, log_set(P, E, F))
