# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2015 World Finals - Problem F. Crane Truck
# https://code.google.com/codejam/contest/5224486/dashboard#s=p5
#
# Time:  O(N^2), correct but TLE for PyPy2 (~16 minutes) 
# Space: O(N^2)
#

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
                    dq[self.move-self.shift] = (dq[self.move-self.shift]-1)%MOD
                elif c == 'd':
                    dq[self.move-self.shift] = (dq[self.move-self.shift]+1)%MOD
                elif c == 'b':
                    self.count += 1
                    if self.move == self.shift:
                        dq.appendleft(0)
                        self.shift -= 1
                    self.move -= 1
                elif c == 'f':
                    self.count += 1
                    if self.move-self.shift+1 == len(dq):
                        dq.append(0)
                    self.move += 1
            return dq

        self.count, self.shift, self.move = 0, 0, 0
        self.values = list(get_delta())

def simulate(deltas):
    result = 0
    period, left, right = 1, 0, 0
    for is_loop, delta in deltas:
        if not is_loop:
            left += -delta.shift
            right += len(delta.values)+delta.shift-1
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
            start = curr+delta.shift
            for i, v in enumerate(islice(delta.values,
                                         max(0, -start),
                                         min(len(delta.values), len(non_periodic_area)-start)),
                                  start+max(0, -start)):
                non_periodic_area[i] = (non_periodic_area[i]+v)%MOD
            curr += delta.move
            result += delta.count
            if not is_loop or \
               (0 <= curr < len(non_periodic_area) and non_periodic_area[curr] == 0):  # stop looping
                break
            if has_visited_non_periodic_area and \
               not (0 <= curr < len(non_periodic_area)):  # periodic area
                has_visited_non_periodic_area = False
                if delta.move > 0:
                    assert(curr >= len(non_periodic_area))
                    target = -(len(delta.values)+delta.shift-1) + CIRCLE_SIZE
                    rep = (target-curr-1)//delta.move+1
                    curr += rep*delta.move - CIRCLE_SIZE
                else:
                    assert(curr < 0)
                    target = len(non_periodic_area)-delta.shift - CIRCLE_SIZE
                    rep = -(target-curr-1)//-(delta.move)+1
                    curr += rep*delta.move + CIRCLE_SIZE
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
