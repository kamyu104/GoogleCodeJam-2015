# https://code.google.com/codejam/contest/4224486/dashboard#s=p2
import math

for c in xrange(input()):
  tree_count = int(raw_input())
  dims = []
  for t in xrange(tree_count):
  	dims.append(map(int, raw_input().strip().split()))

  print "Case #{}:".format(c+1)
  for i, p in enumerate(dims):
  	rest = [d for d in dims if d[0] != p[0] or d[1] != p[1]]
  	angles = [math.atan2(r[1]-p[1], r[0]-p[0]) for r in rest]
  	angles = angles + [a + 2*math.pi for a in angles] + [a + 4*math.pi for a in angles]
  	angles.sort()
  	end = 0

  	min_remove = float("inf")
  	for start in xrange(len(angles) / 2):
  		while angles[end] < (angles[start] + math.pi - 1e-12):
  			end += 1
  		min_remove = min(min_remove, end - start - 1)
  	if min_remove == float("inf"):
  		min_remove = 0
  	print min_remove
