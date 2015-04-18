for cas in xrange(1,1+input()):
	n = input()
	m = map(int, raw_input().strip().split())
	a = sum(max(0, m[i-1]-m[i]) for i in xrange(1,n))
	rate = max(max(0, m[i-1]-m[i]) for i in xrange(1,n))
	b = sum(min(rate, m[i]) for i in xrange(n-1))
	print "Case #%d: %s %s" % (cas, a, b)
