# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 2 - Problem B. Kiddie Pool
# https://code.google.com/codejam/contest/8234486/dashboard#s=p1
#
# Time:  O(NlogN)
# Space: O(1)
#

from sys import float_info

def kiddie_pool():
    C, R = 0, 1
    N, V, X = map(float, raw_input().strip().split())
    N = int(N)
    sources = [map(float, raw_input().strip().split()) for _ in xrange(N)]
    sources = [[(x[1]-X), x[0]] for x in sources]
    
    # Turning on all the sources and get current C.
    cur_C = sum(x[R] * x[C] for x in sources)
    # The rate of turning on all the sources.
    Rmax = sum(x[R] for x in sources)
    if abs(cur_C) > float_info.epsilon:
        sources = sorted(sources, reverse = cur_C > float_info.epsilon)
        
        # For better precision. Recompute Rmax.
        # Rmax = sum(Rj), where j in xrange(i, len(sources))
        # Ri may be slowed down.
        def r_max(sources, i):
            Rmax, cur_C = 0, 0
            # Sum R from i + 1 to len(sources) - 1.
            for j in xrange(i + 1, len(sources)):
                Rmax += sources[j][R]
                cur_C += sources[j][R] * sources[j][C]
            # Check if Ri should be slowed down.
            if abs(sources[i][C]) > float_info.epsilon:
                # 0 = cur_C + Ri' * sources[i][C].
                # Ri' = -cur_C / sources[i][C].
                Rmax += -cur_C / sources[i][C]
            else:
                Rmax += sources[i][R]
            return Rmax
 
        i = 0
        while i < len(sources):
            # Current C is as expected.
            if abs(sources[i][C]) <= float_info.epsilon :
                return V / r_max(sources, i)
            elif (cur_C / sources[i][C]) > float_info.epsilon:
                # To slow down Rmax as little as possible:
                # 1. Always cool down cur_C by slowing down or 
                #    turning off the hotest source i until Ci == 0.
                # 2. Always warm up cur_C by slowing down or 
                #    turning off the coldest source i until Ci == 0.
                if abs(cur_C) > abs(sources[i][R] * sources[i][C]):
                    # Turn off the source i.
                    Rmax -= sources[i][R]
                    # Update current C.
                    cur_C -= sources[i][R] * sources[i][C]
                elif i != len(sources) - 1:
                    # Slow down the source i, the rate is Ri'.
                    return V / r_max(sources, i)
            i += 1
        
        # Turning of all possible sources still does not achieve expected C. 
        return "IMPOSSIBLE"

    return V / Rmax


# Time:  O(N^2)
# Space: O(1)
#
# Minimize Tmax = max(Ti) s.t.
# (1) sum(RiTi) = V
# (2) sum(RiCiTi) = X * V, let Ci be Ci - X => sum(RiCiTi) = 0
def kiddie_pool2():
    R, C = 0, 1
    N, V, X = map(float, raw_input().strip().split())
    N = int(N)
    sources = [map(float, raw_input().strip().split()) for _ in xrange(N)]
    sources = [[x[R], (x[C]-X)] for x in sources]
    
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
