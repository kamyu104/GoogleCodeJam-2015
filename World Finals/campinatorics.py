# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 World Finals - Problem B. Campinatorics
# https://code.google.com/codejam/contest/5224486/dashboard#s=p1
#
# Time:  O(N)
# Space: O(N)
#

MAX_N = 10 ** 6 
modulo = 10 ** 9 + 7

fc = [1]
for i in xrange(1, MAX_N + 1):
    fc.append((fc[-1] * i) % modulo)

fc2 = [pow(z, modulo - 2, modulo) for z in fc]

der = [-1, 0, 1, 1, 3]
for i in xrange(5, MAX_N + 1):
    der.append((der[i - 1] * (i - 1) - der[i - 3] * (i - 4)) % modulo)
der = [(der[i] * fc[i] * (i - 1)) % modulo for i in xrange(len(der))]

def combin(n, k):
    return fc[n] * fc2[k] * fc2[n - k]

# f(N, X) = C(N, X)^2 * X! * ((N-X)! * Dearrangement(N-X))
def f(N, i):
    return ((combin(N, i) ** 2) * fc[i] * der[N - i]) % modulo

def campinatorics(N, X):
    return sum(f(N, i) for i in xrange(X, N + 1)) % modulo

for case in xrange(input()):
    # Read the input.
    N, X = map(int, raw_input().strip().split())
    print "Case #%d: %d" % (case+1, campinatorics(N, X))
