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
    abs_nums = []
    while len(G) > 1:
        Gk = sorted(G.keys())
        num = Gk[1]
        abs_nums.append(num)
        for i in Gk:
            if (i + num) in G:
                G[i + num] -= G[i]
            else:
                G[i + num] = -G[i]
        G = {key:val for (key,val) in G.items() if val != 0}
    
    G = {E[i]-E[0]:F[i] for i in xrange(P)}
    abs_nums = [0] * int(log(G[0], 2)) + abs_nums
    goal = -E[0]
    log_set = []
    for num in abs_nums[::-1]:
        Gk = sorted(G.keys())
        for i in Gk:
            if (i + num) in G:
                G[i + num] -= G[i]
            else:
                G[i + num] = -G[i]
        G = {key:val for (key,val) in G.items() if val != 0}
        if goal + (-num) in G:
            log_set.append(-num)
            goal += -num
        else:
            log_set.append(num)
    log_set.sort()
    return " ".join(map(str, log_set))

for case in xrange(input()):
    # Read the input.
    P = input()
    E = map(int, raw_input().strip().split())
    F = map(int, raw_input().strip().split())

    print "Case #%d: %s" % (case+1, log_set(P, E, F))
