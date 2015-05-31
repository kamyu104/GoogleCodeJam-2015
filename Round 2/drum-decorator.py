# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 2 - Problem D. Drum Decorator
# https://code.google.com/codejam/contest/8234486/dashboard#s=p3
#
# Time:  O(R^2)
# Space: O(R)
#


# In a 1xC, it must be all 2s if previous row is all 3s
#
# In a 2xC, if previous row is all 3s:
# if C % 3 == 0, it can be:
#  221
#  221
# if C % 6, it can be:
# 122221
# 221122
#
# In a 2xC, if previous row is 1s and 2s:
# 333
# 333
#
# In a 3xC, if previous row is all 3s:
# if C % 4 == 0, it can be:
# 1222
# 1212
# 2212
#
from fractions import gcd

def addin(dict, key, value):
    if key in dict:
        dict[key] += value
    else:
        dict[key] = value

def lcm(a,b):
    return (a*b)/gcd(a,b)

def drum_decorator():
    type_1_2, type_3 = 0, 1
    R, C = map(int, raw_input().strip().split())
    states = [{(type_1_2,1):1,(type_3,1):1}]+[{} for i in xrange(R)]
    for i in xrange(R):
        for (type, degree) in states[i]:
            if type == type_1_2:  # previous one is the type of 1s and 2s decoration.
                if (i + 2) <= R:  # 2 rows with 3s
                    addin(states[i+2], (type_3, degree), states[i][(type, degree)])
            else:  # previous one is the type of 3s decoration.
                if (i + 1) <= R:   # 1 rows with all 2s
                    addin(states[i+1], (type_1_2, degree), states[i][(type, degree)])
                if (i + 2) <= R:  # 2 rows with 1s and 2s
                    if (C % 3) == 0:  # Type 1, 3 degree to rotate
                        addin(states[i + 2], (type_1_2, lcm(degree, 3)), 3 * states[i][(type, degree)])
                    if (C % 6) == 0:  # Type 2, 6 degree to rotate
                        addin(states[i + 2], (type_1_2, lcm(degree, 6)), 6 * states[i][(type, degree)])
                if (i + 3) <= R:  # 3 rows with 1s and 2s
                    if (C % 4) == 0:  # 4 degree to rotate
                        addin(states[i + 3], (type_1_2, lcm(degree, 4)), 4 * states[i][(type, degree)])
    ans = 0
    for (type, degree) in states[-1]:
        ans += states[R][(type, degree)]/degree  # Divided by rotate degree.
        ans %= 10**9+7
    return ans


for case in xrange(input()):
    print "Case #%d: %s" % (case+1, drum_decorator())

