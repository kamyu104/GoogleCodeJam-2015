# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 2 - Problem B. Kiddie Pool
# https://code.google.com/codejam/contest/8234486/dashboard#s=p1
#
# Time:  O(N^2)
# Space: O(N)
#

# Minimize max(T_i) s.t.
# sum(R_i * T_i) = V
# sum(R_i * C_i * T_i) = X * V <=> sum(R_i * (C_i - X) * T_i) = 0

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
                # For each Cx find Tx
                # 1. RxTx + sum(RiTi) = V
                # 2. RxTxCx + sum(RiTi) = 0 <=> RxTx + sum(RiTiCi/Cx) = 0
                # 1 - 2: V = sum(RiTi(1 - Ci/Cx)) <= Tmax * sum(Ri(1 - Ci/Cx))
                # <=> V / Tmax <= sum(Ri(1 - Ci/Cx)) = Rx
                # <=> V / Rx <= Tmax
                # To minimize Tmax, is to maximize every Rx.
                Rx = sum(max(0, i[R]*(1-i[C]/Cx)) for i in sources)
                Tx = V / Rx
                Tmax = max(Tmax, Tx)
        if not Tmax:  # Every x[R]*x[C] is zero
            Tmax = V / sum(x[R] for x in sources)
        return Tmax

    return "IMPOSSIBLE"


for case in xrange(input()):
    print "Case #%d: %s" % (case+1, kiddie_pool())
