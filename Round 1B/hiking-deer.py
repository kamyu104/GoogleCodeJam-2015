# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 1B - Problem C. Hiking Deer
# # https://code.google.com/codejam/contest/8224486/dashboard#s=p2
#
# Time:  O(HlogH)
# Space: O(H)
#

import heapq

def hiking_deer():
    heap = []
    hikers = 0
    for i in xrange(input()):
        d, h, m = map(int, raw_input().strip().split())
        for circle_t in xrange(m, m+h):
            t = circle_t * (360-d) / 360.0
            heapq.heappush(heap, (t, 1, circle_t))
            hikers += 1

    current = hikers
    encounters = current
    # At most 2H times to find min encounters.
    # undertake <= H, overtake <= H,
    # current = undertak + overtack <= 2H
    while current <= hikers*2:
        t, d, circle_t = heapq.heappop(heap)
        current -= d
        encounters = min(encounters, current)
        heapq.heappush(heap, (t+circle_t, -1, circle_t))
        
for case in xrange(input()):
    print("Case #%d: %s" % (case+1, hiking_deer()))
