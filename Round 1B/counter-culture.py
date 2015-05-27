# https://code.google.com/codejam/contest/8224486/dashboard
import sys

def reverse(nr):
    return int(str(nr)[::-1])

for case in xrange(input()):
    n = int(raw_input())
    count = 0
    while n > 0:
        digits = str(n)
        halfcount = (len(digits)+1)//2
        rev = reverse(n)
        mod = n % (10 ** halfcount)

        if mod == 1 and n != rev:
            n = rev
            count += 1
        elif mod <= 1:
            n -= 1
            count += 1
        else:
            n -= (mod-1)
            count += (mod-1)

    print("Case #%d: %s" % (case+1, count))
