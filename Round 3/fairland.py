# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round C - Problem A. Fairland
# https://code.google.com/codejam/contest/4254486/dashboard#s=p0
#
# Time:  O(NlogN)
# Space: O(N)
#

def fairland(N, D, S, M):
    max_salary = [0] * N  # max_salary[i]: max salary of the employee i's bosses and himself.
    min_salary = [0] * N  # min_salary[i]: min salary of the employee i's bosses and himself.
    max_salary[0] = S[0]
    min_salary[0] = S[0]
    for i in xrange(1, N):
        max_salary[i] = max(max_salary[M[i]], S[i])
        min_salary[i] = min(min_salary[M[i]], S[i])

    # Employee i can still be hired with range [salary, salary + D] 
    # if and only if min_salary[i] >= salary and max_salary[i] <= salary + D
    salary_count= {}
    for i in xrange(N):
        if min_salary[i] >= max_salary[i] - D:
            # When salary = max_salary[i] - D, hire the employee i.
            if max_salary[i] - D in salary_count:
                salary_count[max_salary[i] - D] += 1
            else:
                salary_count[max_salary[i] - D] = 1
            # When salary = min_salary[i] + 1, fire the employee i.
            if min_salary[i] + 1 in salary_count:
                salary_count[min_salary[i] + 1] -= 1
            else:
                salary_count[min_salary[i] + 1] = -1
    salary_count= sorted([(salary, count) for (salary, count) in salary_count.items()])

    # Count and Find the max number of the employees
    # by increasing salary.
    max_num, num = 0, 0
    for (salary, count) in salary_count:
        num += count
        max_num = max(max_num, num)
    return max_num

for case in xrange(input()):
    # Read the input.
    N, D = map(int, raw_input().strip().split())
    S0, As, Cs, Rs = map(int, raw_input().strip().split())
    M0, Am, Cm, Rm = map(int, raw_input().strip().split())

    S, M = [S0], [M0]
    for _ in xrange(N - 1):
        S.append((S[-1] * As + Cs) % Rs)
        M.append((M[-1] * Am + Cm) % Rm)
    M = [0] + [M[i] % i for i in xrange(1, N)]

    print "Case #%d: %d" % (case+1, fairland(N, D, S, M))
