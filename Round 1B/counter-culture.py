# https://code.google.com/codejam/contest/8224486/dashboard
# Time:  O(nlogn)
# Space: O(1)

import sys

def reverse(nr):
    return int(str(nr)[::-1])

for case in xrange(input()):
    n = int(raw_input())
    count = 0
    while n > 0:
        digits = str(n)
        half_count = (len(digits)+1)//2
        rev_n = reverse(n)
        mod = n % (10 ** half_count)

        if mod == 1 and n != rev_n: # 999001 => 100999
            n = rev_n
            count += 1
        elif mod <= 1: # 100001 => 100000, 100000 => 99999
            n -= 1
            count += 1
        else: # 100999 => 100001
            n -= (mod-1)
            count += (mod-1)
    print("Case #%d: %s" % (case+1, count))
