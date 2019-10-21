# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2015 World Finals - Problem F. Crane Truck
# https://code.google.com/codejam/contest/5224486/dashboard#s=p5
#
# Time:  O(N^2), pass in C++ but PyPy2 (~25 minutes) 
# Space: O(N^2)
#

# N = 2000
# A: [0-2000, 0+2000], [] is the red area modified A
# B: ****[-2000-4001, 2000+4001]****
#    => ****(-6001, 6001)****,
#    * is repeated area modified by B with period pb = O(2B+1) at most 4001,
#    each circle B updates (-6001, 6001) from new computed start point,
#    run at most 4001 * 256 full circles to reach at initial point and stop
#    (increase every point by 256 in full non-periodic area)
# C: ****[-6001-2000, 6001+2000]****,
#    => ****[-8001, 8001]****, [] is the green area modified by C
# D: @@@@[-8001-(4001)^2, 8001+(4001)^2]@@@@,
#    => @@@@[-16016002, 16016002]@@@@
#    @ is repeated area with period pd = lcm(O(2B+1), O(2D+1)) at most 4001^2,
#    each circle D updates {-16016002, 16016002} from new computed start point,
#    run at most 4001^2 * 256 full circles to reach at initial point and stop,
#    (increase every point by 256 in full non-periodic area)
# E: @@@@[-16016002-2000, 16016002+2000]@@@@
#    => @@@@[-16018002, 16018002]@@@@, [] is the last area modified by E
# [Time]
# - A + 256*(2*B+1)*(A + 2*B+1) + C + 256 * (A + (2*B+1) + C + (2B+1)(2D+1)) + E
#   => O(256 * N^2)
# [Space]
# - 2(A + (2*B+1) + C + (2B+1)(2D+1) + E) + 1 <= 2(N + (2N+1) + N + (2N+1)^2 + N) + 1
#   = 2(4N^2+9N)+5 = 32036005
#   => O(8 * N^2)

from collections import deque
from itertools import islice

def lcm(a, b):
    def gcd(a, b):  # Time: O((logn)^2)
        while b:
            a, b = b, a % b
        return a

    return a//gcd(a, b)*b

class Delta(object):
    def __init__(self, instruction):
        def get_delta():
            dq = deque([0])
            for c in instruction:
                if c == 'u':
                    dq[self.shift-self.left] = (dq[self.shift-self.left]-1)%MOD
                elif c == 'd':
                    dq[self.shift-self.left] = (dq[self.shift-self.left]+1)%MOD
                elif c == 'b':
                    self.count += 1
                    if self.shift == self.left:
                        dq.appendleft(0)
                        self.left -= 1
                    self.shift -= 1
                elif c == 'f':
                    self.count += 1
                    if self.shift-self.left+1 == len(dq):
                        dq.append(0)
                    self.shift += 1
            return dq

        self.count, self.left, self.shift = 0, 0, 0
        self.values = list(get_delta())

def simulate(deltas):
    result = 0
    period, left, right = 1, 0, 0
    for is_loop, delta in deltas:
        if not is_loop:
            left += -delta.left
            right += len(delta.values)+delta.left-1
        else:
            period = lcm(period, len(delta.values))
            left += period
            right += period
    curr, non_periodic_area = left, [0]*(left+1+right)
    for is_loop, delta in deltas:
        has_visited_non_periodic_area = False
        while True:
            if 0 <= curr < len(non_periodic_area):
                has_visited_non_periodic_area = True
            start = curr+delta.left
            for i, v in enumerate(islice(delta.values,
                                         max(0, -start),
                                         min(len(delta.values), len(non_periodic_area)-start)),
                                  start+max(0, -start)):
                non_periodic_area[i] = (non_periodic_area[i]+v)%MOD
            curr += delta.shift
            result += delta.count
            if not is_loop or \
               (0 <= curr < len(non_periodic_area) and non_periodic_area[curr] == 0):  # stop looping
                break
            if has_visited_non_periodic_area and \
               not (0 <= curr < len(non_periodic_area)):  # periodic area
                has_visited_non_periodic_area = False
                if delta.shift > 0:
                    assert(curr >= len(non_periodic_area))
                    target = -(len(delta.values)+delta.left-1) + CIRCLE_SIZE
                    rep = (target-curr-1)//delta.shift+1
                    curr += rep*delta.shift - CIRCLE_SIZE
                else:
                    assert(curr < 0)
                    target = len(non_periodic_area)-delta.left - CIRCLE_SIZE
                    rep = -(target-curr-1)//-(delta.shift)+1
                    curr += rep*delta.shift + CIRCLE_SIZE
                result += rep*delta.count
    return result

def crane_truck():
    P = raw_input().strip()
    deltas = []
    i, j = 0, P.find('(')
    while i != len(P) and j != -1:
        if i != j:
            deltas.append((False, Delta(P[i:j])))
        i, j = j+1, P.find(')', j+1)
        deltas.append((True, Delta(P[i:j])))
        i, j = j+1, P.find('(', j+1)
    if i != len(P):
        deltas.append((False, Delta(P[i:])))
    return simulate(deltas)

MOD = 256
CIRCLE_SIZE = 2**40
for case in xrange(input()):
    print "Case #%d: %s" % (case+1, crane_truck())
