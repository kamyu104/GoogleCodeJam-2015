# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Qualification Round - Problem C. Dijkstra
# https://code.google.com/codejam/contest/6224486/dashboard#s=p2
#
# Time:  O(L)
# Space: O(L)
#

multiplicative = { '1':{'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
                   'i':{'1': 'i', 'i':'-1', 'j': 'k', 'k':'-j'},
                   'j':{'1': 'j', 'i':'-k', 'j':'-1', 'k': 'i'},
                   'k':{'1': 'k', 'i': 'j', 'j':'-i', 'k':'-1'},
                  '-1':{'1':'-1', 'i':'-i', 'j':'-j', 'k':'-k'},
                  '-i':{'1':'-i', 'i': '1', 'j':'-k', 'k': 'j'},
                  '-j':{'1':'-j', 'i': 'k', 'j': '1', 'k':'-i'},
                  '-k':{'1':'-k', 'i':'-j', 'j': 'i', 'k': '1'}}

def dijkstra():
    L, X = map(int, raw_input().split())
    S = raw_input()
    
    # Every four copies of anything mutilply to 1, so we can reduce mod 4
    # at most we need 4 copies in each of the first two splits
    # i.e. at most 4 copies of S for mupltiplying to i, 4 copes of S to j,
    #      and the remaining (X % 4) copies of S to k).
    if X >= 8:
        X = 4 + 4 + X % 4
    S *= X

    state, a = 0, '1'
    for b in S:
        a = multiplicative[a][b]
        if state == 0 and a == 'i':
            state = 1  # (i) * remaining
        elif state == 1 and a == 'k':
            state = 2  # (i * j) * remaining

    if state == 2 and a == '-1':
        return "YES"
    else:
        return "NO"

for case in xrange(input()):
    print "Case #{:d}: {:s}".format(case+1, dijkstra())
