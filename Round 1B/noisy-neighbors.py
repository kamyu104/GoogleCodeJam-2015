# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 1B - Problem B. Noisy Neighbors
# https://code.google.com/codejam/contest/8224486/dashboard#s=p1
#
# Time:  O(R * C)
# Space: O(1)
#
# It does exist Time: O(1) solution, but the formula is error-prone, 
# hard to figure out it during the contest time.
#

def unhappiness(R, C, N):
    answer = 0
    if N > (R * C + 1) / 2:
        vacant_num = R * C - N
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # Number of rooms for each edge number.
        rooms = [[0 for _ in xrange(5)] for _ in xrange(2)]
        for i in xrange(R):
            for j in xrange(C):
                count = 0
                for d in directions:
                    if i + d[0] < 0 or i + d[0] >= R or \
                        j + d[1] < 0 or j + d[1] >= C:
                        continue
                    count += 1
                rooms[(i+j)%2][count] += 1

        # Max edge number of vacant even rooms.
        even_edges, remaining = 0, vacant_num
        for count in reversed(xrange(5)):
            even_edges += count * min(rooms[0][count], remaining)
            remaining -= min(rooms[0][count], remaining)
        
        # Max edge number of vacant odd rooms.
        odd_edges, remaining = 0, vacant_num
        for count in reversed(xrange(5)):
            odd_edges += count * min(rooms[1][count], remaining)
            remaining -= min(rooms[1][count], remaining)

        # (total edge number) - (max edge numbers of vacant rooms).
        answer = (R * (C - 1) + (R - 1) * C) - max(even_edges, odd_edges)
    return answer

for case in xrange(input()):
    R, C, N = map(int, raw_input().strip().split())
    print("Case #%d: %d" % (case+1, unhappiness(R, C, N)))
