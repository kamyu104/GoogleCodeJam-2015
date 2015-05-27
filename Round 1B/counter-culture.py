# https://code.google.com/codejam/contest/8224486/dashboard
# Time:  O(logn)
# Space: O(logn), for reversed string

import sys

def reverse(num):
    return int(str(num)[::-1])

for case in xrange(input()):
    n = int(raw_input())
    count = 0
    while n > 0:
        digits = str(n)
        half_count = (len(digits)+1)//2
        reversed_n = reverse(n)
        mod = n % (10 ** half_count)

        if mod == 1 and n != reversed_n: # 999001 => 100999
            n = reversed_n
            count += 1
        elif mod <= 1: # 100001 => 100000, 100000 => 99999
            n -= 1
            count += 1
        else: # 100999 => 100001
            n -= (mod-1)
            count += (mod-1)
    print("Case #%d: %s" % (case+1, count))
