# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 World Finals - Problem D. Taking Over The World
# https://code.google.com/codejam/contest/5224486/dashboard#s=p3
#
# Time:  O(?)
# Space: O(?)
#

from collections import deque
from heapq import heappush, heappop

TO, CAP, REV = 0, 1, 2

def vid(v, o):
    return v * 2 + int(o)


def add_edge(i, j, c, adj):
    adj[i].append([j, c, len(adj[j])])
    adj[j].append([i, 0, len(adj[i]) - 1])


def dijkstra(guard, A, s):
    dst = [float("inf")] * len(A)
    dst[s] = 0
    q = []
    heappush(q, (0, s))
    while q:
        c, v = heappop(q);
        if dst[v] == c:
            for tv in xrange(len(A[v])):
                if A[v][tv]:
                    tc = dst[v] + 1 + int(guard[v]);
                    if tc < dst[tv]:
                        dst[tv] = tc
                        heappush(q, (tc, tv))
    return dst


def levelize(V, S, T, adj, lev):
    for i in xrange(V):
        lev[i] = -1
    lev[S] = 0
    q = deque([S])
    while q:
        v = q.popleft()
        for i in xrange(len(adj[v])):
            to, cap, rev = adj[v][i]
            if cap and lev[to] == -1:
                lev[to] = lev[v] + 1
                q.append(to)

    return lev[T] != -1


def augment(S, T, v, f, lev, adj, done):
    if v == T or not f:
        return f
    while done[v] < len(adj[v]):
        to, cap, rev = adj[v][done[v]]
        if lev[to] > lev[v]:
            t = augment(S, T, to, min(f, cap), lev, adj, done)
            if t > 0:
                adj[v][done[v]][CAP] -= t
                adj[to][rev][CAP] += t
                return t
        done[v] += 1

    return 0


def max_flow(V, S, T, adj):
    f, t = 0, 0
    lev = [-1] * V
    while levelize(V, S, T, adj, lev):
        done = [0] * V
        t = float("inf")
        while t:
            t = augment(S, T, S, float("inf"), lev, adj, done)
            f += t

    return f


def min_cut(V, S, adj):
    vis = [False] * V;
    vis[S] = True;
    q = deque([S]);
    while q:
        v = q.popleft();
        for to, cap, rev in adj[v]:
            if cap and not vis[to]:
                q.append(to)
                vis[to] = True

    return vis


def taking_over_the_world():
    N, M, K = map(int, raw_input().strip().split())
    A = [[0 for _ in xrange(N)] for _ in xrange(N)]
    for i in xrange(M):
        u, v = map(int, raw_input().strip().split())
        A[u][v] = A[v][u] = True

    GUARD = 1000
    guard = [False] * N
    while True:
        V, S, T = N * 2, vid(0, False), vid(N - 1, False)
        adj = [[] for _ in xrange(V)]
        for v in xrange(N):
            add_edge(vid(v, False), vid(v, True), GUARD if guard[v] else 1, adj)

        ds, dt = dijkstra(guard, A, 0), dijkstra(guard, A, N - 1);
        for u in xrange(N):
            for v in xrange(N):
                if A[u][v]:
                    if ds[u] != -1 and dt[v] != -1:
                        # Edge (u, v)
                        td = (ds[u] + int(guard[u])) + \
                             1 + \
                             (0 if v == N - 1 else int(guard[v]) + dt[v])
                        if td == ds[N - 1]:
                            add_edge(vid(u, True), vid(v, False), GUARD, adj)

        if max_flow(V, S, T, adj) <= K:
            mc = min_cut(V, S, adj)
            for v in xrange(N):
                if mc[vid(v, False)] and  not mc[vid(v, True)]:
                    guard[v] = True
                    K -= 1
        else:
            break

    return dijkstra(guard, A, 0)[N - 1]


for case in xrange(input()):
    print "Case #%d: %d" % (case+1, taking_over_the_world())
