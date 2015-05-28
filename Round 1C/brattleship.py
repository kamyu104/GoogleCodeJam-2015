# https://code.google.com/codejam/contest/4244486/dashboard
# Time:  O(1)
# Space: O(1)

def score(R, C, W):
    # 1. The move to find the correct row where battleshipt:
    #    (R - 1) * (C // W)
    #
    # 2. The move to find the whole battle ship in the last row:
    #    case C % W == 0:
    #        C // W - 1 + W
    #    case C % W != 0:
    #        C // W + W
    #    =>  (C - 1) // W + W
    return ((R - 1) * (C // W)) + ((C - 1) // W + W)

for case in xrange(input()):
    (R, C, W) = map(int, raw_input().strip().split())
    print "Case #%d: %d" % (case+1, score(R, C, W))
