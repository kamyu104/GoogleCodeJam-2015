# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2015 World Finals - Problem F. Crane Truck
# https://code.google.com/codejam/contest/5224486/dashboard#s=p5
#
# Time:  O(N^2), N is the length of the program, pass in PyPy2 but Python2
# Space: O(N^2)
#

from collections import deque

def lcm(a, b):
    def gcd(a, b):  # Time: O((logn)^2)
        while b:
            a, b = b, a % b
        return a

    return a//gcd(a, b)*b

class Delta(object):
    def __init__(self, instructions):
        def find_delta():
            dq = deque([0])
            base = 0
            # extend delta window
            for c in instructions:
                if c == 'u':
                    dq[self.shift-base] = (dq[self.shift-base]-1)%MOD
                elif c == 'd':
                    dq[self.shift-base] = (dq[self.shift-base]+1)%MOD
                elif c == 'b':
                    self.count += 1
                    if self.shift == base:
                        dq.appendleft(0)
                        base -= 1
                    self.shift -= 1
                elif c == 'f':
                    self.count += 1
                    if self.shift-base+1 == len(dq):
                        dq.append(0)
                    self.shift += 1
            self.left = -base
            self.right = len(dq) - self.left - 1
            # shrink delta window
            while self.left > 0:
                if dq[0] != 0:
                    break
                dq.popleft()
                self.left -= 1
            while self.right > 0:
                if dq[-1] != 0:
                    break
                dq.pop()
                self.right -= 1
            return [(i, v) for i, v in enumerate(dq, -self.left) if v != 0]  # save sparse delta window

        self.count, self.shift, self.left, self.right = 0, 0, 0, 0
        self.values = find_delta()

def simulate(deltas):
    result = 0
    period, left, right = 1, 0, 0
    for is_loop, delta in deltas:  # extend non-periodic area
        if not (is_loop and delta.shift):
            left += max(delta.left, -delta.shift if delta.shift < 0 else 0)
            right += max(delta.right, delta.shift if delta.shift > 0 else 0)
        else:
            period = lcm(period, abs(delta.shift))
            if delta.shift < 0:
                if delta.left >= -delta.shift:
                    left += delta.left - (1+delta.left)%-delta.shift
                left += period
                right += delta.right
            else:
                if delta.right >= delta.shift:
                    right += delta.right - (1+delta.right)%delta.shift
                right += period
                left += delta.left
    curr, non_periodic_area = left, [0]*(left+1+right)  # Space: O(N^2)
    for is_loop, delta in deltas:
        has_visited_non_periodic_area = False
        while True:  # Time: O(256 * N^2)
            if not has_visited_non_periodic_area and 0 <= curr < len(non_periodic_area):
                has_visited_non_periodic_area = True
            for i, v in delta.values:
                if 0 <= curr+i < len(non_periodic_area):
                    non_periodic_area[curr+i] = (non_periodic_area[curr+i]+v)%MOD
            curr += delta.shift
            result += delta.count
            if not is_loop or \
               (0 <= curr < len(non_periodic_area) and non_periodic_area[curr] == 0):  # stop looping
                break
            if has_visited_non_periodic_area and \
               not (0 <= curr < len(non_periodic_area)):  # pass through periodic area
                has_visited_non_periodic_area = False
                if delta.shift > 0:
                    assert(curr >= len(non_periodic_area))
                    target = -delta.right + CIRCLE_SIZE
                    rep = (target-curr-1)//delta.shift + 1
                    curr += rep*delta.shift - CIRCLE_SIZE
                else:
                    assert(curr < 0)
                    target = (len(non_periodic_area)-1) + delta.left - CIRCLE_SIZE
                    rep = (curr-target-1)//-delta.shift + 1
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
