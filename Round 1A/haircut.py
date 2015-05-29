# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 1A - Problem B. Haircut
# https://code.google.com/codejam/contest/4224486/dashboard#s=p1
#
# Time:  O(log(N * max(M)) + BlogB)
# Space: O(B)
#

def haircut():
    b, n = map(int, raw_input().strip().split())
    m = map(int, raw_input().strip().split())
    # Count the number of coming guests at the time T.
    def guest_num(T):
    	s = 0
    	for i in xrange(b):
    	    s += (T + m[i]-1) // m[i]
        return s

    # Time:  O(log(N * max(M)))
    # Find the most time when the number of guests is still less than n
    L = 0
    R = 10**14
    while  L <= R:
        M = L + R >> 1
        if guest_num(M) >= n:
            R = M - 1
        else:
            L = M + 1

    # Now guest_num(L-1) < n <= guest_num(L)
    # At the time L, the number of coming guest achieves n.
    time_to_available = [0]*b
    for i in xrange(b):
        ct = (L-1 + m[i] - 1) // m[i]
        time_to_available[i] = ct * m[i]
        n -= ct
    
    # Time:  O(BlogB)
    # Sort time_to_available by time and id,
    # assign the remaining guests to the available ones by id order at the time L.
    # Now 0 <= n <= b
    idxs = sorted(xrange(b), key=lambda i: (time_to_available[i], i))

    # (i+1)th barber.
    return idxs[n-1]+1
	
for case in xrange(input()):
    print "Case #%d: %d" % (case+1, haircut())
