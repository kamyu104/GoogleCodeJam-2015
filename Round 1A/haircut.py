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
    def f(T):
    	s = 0
    	for i in xrange(b):
    	    s += (T + m[i]-1) // m[i]
	 return s

    # Time:  O(log(N * max(M)))
    # Find the most time when the number of guests is still less than n
    L = -1
    R = 10**14 + 1
    while  R - L > 1:
        M = L + R >> 1
        fM = f(M)
        if fM >= n:
            R = M
        else:
            L = M
    # Now f(L) < n <= f(R)
    assert f(L) < n <= f(R)
    time_to_available = [0]*b
    for i in xrange(b):
        ct = (L + m[i] - 1) // m[i]
        time_to_available[i] = ct * m[i]
        n -= ct
    
    # Time:  O(BlogB)
    # Sort time_to_available by time and id, assign guest to the available one 
    assert 0 <= n <= b
    idxs = sorted(range(b), key=lambda i: (time_to_available[i], i))
	
    return idxs[n-1]+1
	
for case in xrange(input()):
    print "Case #%d: %d" % (case+1, haircut())
