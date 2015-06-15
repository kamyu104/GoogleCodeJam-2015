# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round C - Problem A. Fairland
# https://code.google.com/codejam/contest/4254486/dashboard#s=p0
#
# Time:  O(NlogN)
# Space: O(N)
#

def fairland(N, D, S, M):
    mx = [0] * N  # mx[i]: max salary of employee i's bosses or coworkers.
    mn = [0] * N  # mn[i]: min salary of employee i's bosses or coworkers.
    mx[0] = S[0]
    mn[0] = S[0]
    for i in xrange(1, N):
        mx[i] = max(mx[M[i]], S[i])
        mn[i] = min(mn[M[i]], S[i])

    # Employee i can still be hired with range [z, z+D] 
    # if mn[i] >= z and mx[i] <= z + D
    w = {}
    for i in xrange(N):
        if mn[i] >= mx[i] - D:
            # When z = mx[i] - D, hire = employee i.
            if mx[i] - D in w:
                w[mx[i] - D] += 1
            else:
                w[mx[i] - D] = 1
            # When z = mn[i] + 1, fire the employee i.
            if mn[i] + 1 in w:
                w[mn[i] + 1] -= 1
            else:
                w[mn[i] + 1] = -1
    w = sorted([(z, cnt) for (z, cnt) in w.items()])

    # Count and Find the max number of the employees
    # by increasing z.
    max_num, num = 0, 0
    for (z, cnt) in w:
        num += cnt
        max_num = max(max_num, num)
    return max_num

for case in xrange(input()):
    # Read the input
    N, D = map(int, raw_input().strip().split())
    S0, As, Cs, Rs = map(int, raw_input().strip().split())
    M0, Am, Cm, Rm = map(int, raw_input().strip().split())

    S, M = [S0], [M0]
    for _ in xrange(N - 1):
        S.append((S[-1] * As + Cs) % Rs)
        M.append((M[-1] * Am + Cm) % Rm)
    M = [0] + [M[i] % i for i in xrange(1,N)]

    print "Case #%d: %d" % (case+1, fairland(N, D, S, M))
