# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 World Finals - Problem E. Merlin QA
# https://code.google.com/codejam/contest/5224486/dashboard#s=p4
#
# Time:  O(M! * (N * M))
# Space: O(N * M)
#

from itertools import permutations

# For each permutation of ingredient vector.
def f(spells):
    vals = 0
    for spell in spells:    # Time: O(N)
        val, costs = 0, 0
        # Get max cost sum of spell vector from the beginning.
        for cost in spell:  # Time: O(M)
            costs += cost
            val = max(val, costs)
        vals += val
    return vals

def merlin_qa(N, M, spells):
    spells = [i for i in spells if max(i) > 0]
    if not spells:
        return 0
    largest = 0
    for permutation in permutations(xrange(M)):  # Time: O(M!)
        vals = f([[spell[i] for i in permutation] for spell in spells])
        largest = max(largest, vals)
    return largest

for case in xrange(input()):
    N, M = map(int, raw_input().strip().split())
    spells = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    print "Case #%d: %d" % (case+1, merlin_qa(N, M, spells))

