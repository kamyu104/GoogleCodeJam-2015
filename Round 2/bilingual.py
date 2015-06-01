# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 2 - Problem C. Bilingual
# https://code.google.com/codejam/contest/8234486/dashboard#s=p2
#
# Time:  O(N * W)
# Space: O(N + W)
#

def dfs(node, sink, used, E):
    if used[node]:
        return False
    used[node] = True

    i = 0
    for i in xrange(len(E[node])):
        if E[node][i] == sink or dfs(E[node][i], sink, used, E):
            E[E[node][i]].append(node)
            E[node][-1], E[node][i] = E[node][i], E[node][-1]
            E[node].pop()
            return True
    return False

def word_idx(values, word):
    if word in values:
        return values[word]
    values[word] = len(values)
    return values[word]

def bilingual():
    N = input()
    values = {}
    lines = [list(set([word_idx(values, word) for word in raw_input().strip().split()])) for _ in xrange(N)]
    # Init edges.
    source, sink = 0, 1
    E = [[] for _ in xrange(2*len(values)+N)]
    for i in xrange(len(values)):
        E[2*i+N].append(2*i+N+1)
    for x in lines[0]:
        E[source].append(2*x+N)
    for y in lines[1]:
        E[2*y+N+1].append(sink)
    for i in xrange(2, N):
        for x in lines[i]:
            E[2*x+N+1].append(i)
            E[i].append(2*x+N)
    # Run max flow.
    flow = 0
    used = [False for _ in xrange(len(E))]
    while dfs(source, sink, used, E):
        flow += 1
        used = [False for _ in xrange(len(E))]
    return flow


for case in xrange(input()):
    print "Case #%d: %d" % (case+1, bilingual())
