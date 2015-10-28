# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 World Finals - Problem B. Campinatorics
# https://code.google.com/codejam/contest/5224486/dashboard#s=p1
#
# Time:  O(N)
# Space: O(N)
#

MAX_N = 10 ** 6 
prime = 10 ** 9 + 7

fc = [1]
for i in xrange(1, MAX_N + 1):
    fc.append((fc[-1] * i) % prime)

inv_fc = [pow(x, prime - 2, prime) for x in fc]

# D(n) = (n - 1) * (D(i - 1) + D(n - 2))
D = [1, 0]
for i in xrange(2, MAX_N + 1):
    D.append((i - 1) * (D[i - 1] + D[i - 2]) % prime)

# C(n, k) = n! / (k!*(n - k)!) = n! * (k!*(n - k)!)^-1 (mod p)
# For p prime, the inverse of any number x mod p is x^(p - 2) mod p (Euler's Theorem).
def C(n, k):
    return (fc[n] * inv_fc[k] * inv_fc[n - k]) % prime

# f(N, X) = C(N, X)^2 * X! * ((N - X)! * Dearrangement(N - X))
def f(N, X):
    return ((C(N, X) ** 2) * fc[X] * fc[N - X] * D[N - X]) % prime

def campinatorics(N, X):
    return sum(f(N, i) for i in xrange(X, N + 1)) % prime

for case in xrange(input()):
    # Read the input.
    N, X = map(int, raw_input().strip().split())
    print "Case #%d: %d" % (case+1, campinatorics(N, X))
