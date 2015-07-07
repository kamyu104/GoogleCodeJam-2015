# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round C - Problem D. Log Set
# https://code.google.com/codejam/contest/4254486/dashboard#s=p3
#
# Time:  O(N * (logN)^2), N is sum of F
# Space: O(logN)
#

from math import log

def log_set(P, E, F):
    Ei_to_Fi = {E[i]:F[i] for i in xrange(P)}
    abs_elements = []
    
    # Total Time: O(1 + 2log2 + (2^2)log(2^2) + ... NlogN) = O(N * (logN)^2)
    while len(Ei_to_Fi) > 1: # logN times
        Eis = sorted(Ei_to_Fi.keys()) # Time: O(N'logN')
        element = Eis[1] - Eis[0]
        abs_elements.append(element)
        for Ei in Eis:
            # Decrease frequencies of E[i] shifted by element.
            if (Ei + element) in Ei_to_Fi:
                Ei_to_Fi[Ei + element] -= Ei_to_Fi[Ei]
        # print element, Eis, Ei_to_Fi
        # Keep keys which val > 0 to get new log set without current element.
        # This would decrease the sum of frequencies to half of it.
        # Time: O(N')
        Ei_to_Fi = {Ei:Fi for (Ei,Fi) in Ei_to_Fi.items() if Fi != 0}

    Ei_to_Fi = {E[i]:F[i] for i in xrange(P)}
    abs_elements = [0] * int(log(F[0], 2)) + abs_elements
    base, log_set = 0, []
    # print abs_elements[::-1]
    # Reversely enumerate abs_elements to achieve the earliest set.
    for element in abs_elements[::-1]: # logN Times
        Eis = sorted(Ei_to_Fi.keys()) # Time: O(N'logN')
        for i in Eis:
            if (i + element) in Ei_to_Fi:
                Ei_to_Fi[i + element] -= Ei_to_Fi[i]
        # print element, base, Eis, Ei_to_Fi
        # Keep keys which val > 0 to get new set without current element.
        # This would decrease the sum of frequencies to half of it.
        Ei_to_Fi = {Ei:Fi for (Ei,Fi) in Ei_to_Fi.items() if Fi != 0}
        
        # If negative of element could be put to set,
        # add it to achieve the earliest set.
        if base + (-element) in Ei_to_Fi:
            log_set.append(-element)
            base += -element
        else: # element must be positive.
            log_set.append(element)

    # Nondecreasing order.
    log_set.sort()
    return " ".join(map(str, log_set))

for case in xrange(input()):
    # Read the input.
    P = input()
    E = map(int, raw_input().strip().split())
    F = map(int, raw_input().strip().split())
    # print E, F

    print "Case #%d: %s" % (case+1, log_set(P, E, F))
