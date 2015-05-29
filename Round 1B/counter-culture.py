# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 1B - Problem A. Counter Culture
# https://code.google.com/codejam/contest/8224486/dashboard#s=p0
#
# Time:  O(logN), increase 1 digit every 5 loops.
# Space: O(logN), for reversed string
#

def reverse(num):
    return int(str(num)[::-1])

for case in xrange(input()):
    N = int(raw_input())
    
    count = 0
    while N > 0:
        digits = str(N)  
        half_count = (len(digits)+1)//2
        reversed_n = reverse(N) 
        mod = N % (10 ** half_count)

        if mod == 1 and N != reversed_n: # 999001 => 100999
            N = reversed_n
            count += 1
        elif mod <= 1: # 100001 => 100000, 100000 => 99999
            N -= 1
            count += 1
        else: # 100999 => 100001
            N -= (mod-1)
            count += (mod-1)
            
    print("Case #%d: %d" % (case+1, count))
