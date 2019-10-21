# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2015 World Finals - Problem F. Crane Truck
# https://code.google.com/codejam/contest/5224486/dashboard#s=p5
#
# Time:  O(N^2), pass in PyPy2 but Python2
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
    def __init__(self, instruction):
        def get_delta():
            dq = deque([0])
            for c in instruction:
                if c == 'u':
                    dq[self.__end-self.__base] = (dq[self.__end-self.__base]-1)%MOD
                elif c == 'd':
                    dq[self.__end-self.__base] = (dq[self.__end-self.__base]+1)%MOD
                elif c == 'b':
                    self.__count += 1
                    if self.__end == self.__base:
                        dq.appendleft(0)
                        self.__base -= 1
                    self.__end -= 1
                elif c == 'f':
                    self.__count += 1
                    if self.__end-self.__base+1 == len(dq):
                        dq.append(0)
                    self.__end += 1
            return dq

        self.__instruction = instruction
        self.__count, self.__base, self.__end = 0, 0, 0
        self.__values = list(get_delta())

    def left_len(self):
        return -self.__base

    def right_len(self):
        return len(self.__values)+self.__base-1

    def values(self):
        return self.__values

    def move(self):
        return self.__end

    def count(self):
        return self.__count

    def __len__(self):
        return len(self.__values)

def simulate(deltas):
    period, left, right = 1, 0, 0
    for is_loop, delta in deltas:
        if not is_loop:
            left += delta.left_len()
            right += delta.right_len()
        else:
            period = lcm(period, len(delta))
            left += period
            right += period
    zero_position, non_period_area = left, [0]*(left+1+right)
    result, curr = 0, zero_position
    for is_loop, delta in deltas:
        while True:
            for i, v in enumerate(delta.values()):
                if 0 <= curr-delta.left_len()+i < len(non_period_area):
                    non_period_area[curr-delta.left_len()+i] = (non_period_area[curr-delta.left_len()+i]+v)%MOD
            curr += delta.move()
            result += delta.count()
            if not is_loop or \
               (0 <= curr < len(non_period_area) and non_period_area[curr] == 0):
                break
            if not (0 <= curr < len(non_period_area)):
                if delta.move() > 0:
                    target = CIRCULAR_SIZE-delta.right_len()
                    rep = (target-curr-1)//delta.move()+1
                    curr += rep*delta.move() - CIRCULAR_SIZE
                elif delta.move() < 0:
                    target = -CIRCULAR_SIZE+len(non_period_area)+delta.left_len()
                    rep = -(target-curr-1)//-(delta.move())+1
                    curr += rep*delta.move() + CIRCULAR_SIZE
                else:
                    assert(False)
                result += rep*delta.count()
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
CIRCULAR_SIZE = 2**40
for case in xrange(input()):
    print "Case #%d: %s" % (case+1, crane_truck())