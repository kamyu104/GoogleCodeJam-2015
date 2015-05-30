# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 1B - Problem B. Noisy Neighbors
# https://code.google.com/codejam/contest/8224486/dashboard#s=p1
#
# Time:  O(RClogRC)
# Space: O(RC)
#

def unhappiness(R, C, N):
    answer = 0
    if N > (R * C + 1) / 2:
        vacant_num = R * C - N
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        edges = [[], []]
        for i in xrange(R):
            for j in xrange(C):
                count = 0
                for d in directions:
                    if i + d[0] < 0 or i + d[0] >= R or \
                       j + d[1] < 0 or j + d[1] >= C:
                        continue
                    count += 1
                edges[(i + j) % 2].append(count);

        # Sort by the edge number of the room.
        edges[0].sort(reverse=True)
        edges[1].sort(reverse=True)

        # Max edge number of vacant even / odd rooms.
        even_edges, odd_edges = 0, 0
        for i in xrange(vacant_num):
            even_edges += edges[0][i]
            odd_edges += edges[1][i]

        # (total edge number) - (max edge numbers of vacant rooms).
        answer = (R * (C - 1) + (R - 1) * C) - max(even_edges, odd_edges)
    return answer

for case in xrange(input()):
    R, C, N = map(int, raw_input().strip().split())
    print("Case #%d: %d" % (case+1, unhappiness(R, C, N)))
