# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 1C - Problem A. Brattleship
# https://code.google.com/codejam/contest/4244486/dashboard#s=p0
#
# Time:  O(1)
# Space: O(1)
#

def score(R, C, W):
    # 1. The move to find the correct row where the battleship is:
    #    (R - 1) * (C // W)
    #
    # 2. The move to find the whole battle ship in the last row:
    #    case (1) C % W == 0:
    #        C // W - 1 + W = (C - 1) // W + W
    #    case (2) C % W != 0:
    #        C // W + W = (C - 1) // W + W
    #    case (1) + (2) <=> (C - 1) // W + W
    return ((R - 1) * (C // W)) + ((C - 1) // W + W)

for case in xrange(input()):
    R, C, W = map(int, raw_input().strip().split())
    print "Case #%d: %d" % (case+1, score(R, C, W))
