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
# sum(R_i * C_i * T_i) = X * V => sum(R_i * (C_i - X) * T_i) = 0

def kiddie_pool():
    R, C = 0, 1
    N, V, X = map(float, raw_input().strip().split())
    N = int(N)
    sources = [map(float, raw_input().strip().split()) for i in xrange(N)]
    sources = [(source[0], (source[1]-X)) for source in sources]
    T = "IMPOSSIBLE"
    
    if max((source[R]*source[C]) for source in sources) >= 0 and \
       min((source[R]*source[C]) for source in sources) <= 0:
        T = V / sum(source[R] for source in sources)
        for source in sources:
            if (source[R]*source[C]) != 0:
                Cx = source[C]
                # For each Cx find Tx
                # RxTx + sum(RiTi) = V
                # CxRxTx + sum(CiRiTi) = 0
                # => V = sum(Ri(1 - Ci/Cx)Ti) <= Tmax * sum(Ri(1 - Ci/Cx))
                # => Rx = V / Tmax <= sum(Ri(1 - Ci/Cx))
                # Rx <= sum(source[R]*(1 - source[C]/Cx))
                # To minimize Tmax, is to maximize Rx.
                Rx = sum(max(0, source[R]*(1-source[C]/Cx)) for source in sources)
                T = max(T, V / Rx)
    return T


for case in xrange(input()):
    print "Case #%d: %s" % (case+1, kiddie_pool())
