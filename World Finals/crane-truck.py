# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2015 World Finals - Problem F. Crane Truck
# https://code.google.com/codejam/contest/5224486/dashboard#s=p5
#
# Time:  O(N^2), pass in PyPy2 but Python2
# Space: O(N^2)
#

# [Analysis]
#  - N = 2000
#  - A: [0-2000, 0+2000], [] is the red area modified A
#  - B: ****[-2000-4001, 2000+4001]****
#    => ****(-6001, 6001)****,
#    * is repeated area modified by B with period pb = O(2B+1) at most 4001,
#    each circle B updates (-6001, 6001) from new computed start point,
#    run at most 4001 * 256 full circles to reach at initial point and stop
#    (increase every point by 256 in full non-periodic area)
#  - C: ****[-6001-2000, 6001+2000]****,
#    => ****[-8001, 8001]****, [] is the green area modified by C
#  - D: @@@@[-8001-(4001)^2, 8001+(4001)^2]@@@@,
#    => @@@@[-16016002, 16016002]@@@@
#    @ is repeated area with period pd = lcm(O(2B+1), O(2D+1)) at most 4001^2,
#    each circle D updates {-16016002, 16016002} from new computed start point,
#    run at most 4001^2 * 256 full circles to reach at initial point and stop,
#    (increase every point by 256 in full non-periodic area)
#  - E: @@@@[-16016002-2000, 16016002+2000]@@@@
#    => @@@@[-16018002, 16018002]@@@@, [] is the last area modified by E
# [Time]
#  - 1 + A + 256 * (1 + A + B) + C + 256 * (1 + A + B + C + B*D) + E
#    => O(256 * N^2)
# [Space]
#  - 1 + A + B + C + B*D + E <= 1 + (N + N + N + N^2 + N)
#    = N^2 + 4*N + 1= 4008001
#    => O(N^2)

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
        left += delta.left
        right += delta.right
        if is_loop and delta.shift:
            period = lcm(period, abs(delta.shift))
            if delta.shift < 0:
                left += period - (delta.left+1)%-delta.shift
            else:
                right += period - (1+delta.right)%delta.shift
    curr, non_periodic_area = left, [0]*(left+1+right)
    for is_loop, delta in deltas:
        has_visited_non_periodic_area = False
        while True:
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
