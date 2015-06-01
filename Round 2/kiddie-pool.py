# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 2 - Problem B. Kiddie Pool
# https://code.google.com/codejam/contest/8234486/dashboard#s=p1
#
# Time:  O(N^2)
# Space: O(1)
#

from sys import float_info

# Minimize Tmax = max(Ti) s.t.
# (1) sum(RiTi) = V
# (2) sum(RiCiTi) = X * V, let Ci be Ci - X => sum(RiCiTi) = 0
def kiddie_pool():
    R, C = 0, 1
    N, V, X = map(float, raw_input().strip().split())
    N = int(N)
    sources = [map(float, raw_input().strip().split()) for _ in xrange(N)]
    sources = [[i[0], (i[1]-X)] for i in sources]
    
    # Rx always > 0, no need to care special case.
    if max(x[C] for x in sources) >= -float_info.epsilon and \
       min(x[C] for x in sources) <= float_info.epsilon:
        Tmax = V / sum(x[R] for x in sources) # This is the min of Tmax,
                                              # only happens if every x[R]*x[C] is zero
        for x in sources:
            if abs(x[C]) > float_info.epsilon:
                # For each Cx find Tx by the following:
                # (1) V = RxTx   + sum(RiTi),     (sum() for each i != x)
                # (2) 0 = RxTxCx + sum(RiTiCi),   (sum() for each i != x)
                # <=> 0 = RxTx + sum(RiTiCi/Cx)
                # (1) - (2): V = sum(RiTi(1 - Ci/Cx)) <= Tmax * sum(Ri(1 - Ci/Cx))
                # <=> V / Tmax <= sum(Ri(1 - Ci/Cx)) = Fx
                # <=> V / Fx <= Tmax
                # To minimize Tmax, is to maximize every Fx, i.e minimize every Tx = V / Fx.
                Fx = sum(max(0, i[R]*(1-i[C]/x[C])) for i in sources)
                Tx = V / Fx
                Tmax = max(Tmax, Tx)
        return Tmax

    # Every Ci > 0 or every Ci < 0.
    return "IMPOSSIBLE"


for case in xrange(input()):
    print "Case #%d: %s" % (case+1, kiddie_pool())
