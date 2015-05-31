# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 2 - Problem B. Kiddie Pool
# https://code.google.com/codejam/contest/8234486/dashboard#s=p1
#
# Time:  O(N^2)
# Space: O(N)
#

# Minimize Tmax = max(Ti) s.t.
# (1) sum(RiTi) = V
# (2) sum(RiCiTi) = X * V, let Ci be Ci - X => sum(RiCiTi) = 0

def kiddie_pool():
    R, C = 0, 1
    N, V, X = map(float, raw_input().strip().split())
    N = int(N)
    sources = [map(float, raw_input().strip().split()) for i in xrange(N)]
    sources = [(source[0], (source[1]-X)) for source in sources]
    
    if max((x[R]*x[C]) for x in sources) >= 0 and \
       min((x[R]*x[C]) for x in sources) <= 0:
        Tmax = None
        for x in sources:
            if (x[R]*x[C]) != 0:
                Cx = x[C]
                # For each Cx find Tx by the following:
                # (1) V = KxTx   + sum(RiTi),     (sum() for each i != x)
                # (2) 0 = KxTxCx + sum(RiTiCi),   (sum() for each i != x)
                # <=> 0 = KxTx + sum(RiTiCi/Cx)
                # (1) - (2): V = sum(RiTi(1 - Ci/Cx)) <= Tmax * sum(Ri(1 - Ci/Cx))
                # <=> V / Tmax <= sum(Ri(1 - Ci/Cx)) = Kx
                # <=> V / Kx <= Tmax
                # To minimize Tmax, is to maximize every Kx, i.e minimize every Tx = V / Kx .
                Kx = sum(max(0, i[R]*(1-i[C]/Cx)) for i in sources)
                Tx = V / Kx
                Tmax = max(Tmax, Tx)
        if not Tmax:  # Every x[R]*x[C] is zero
            Tmax = V / sum(x[R] for x in sources)
        return Tmax
    else:
        return "IMPOSSIBLE"


for case in xrange(input()):
    print "Case #%d: %s" % (case+1, kiddie_pool())
