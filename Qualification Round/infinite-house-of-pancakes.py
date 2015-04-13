# Problem Description: https://code.google.com/codejam/contest/6224486/dashboard#s=p1

def solve():
    d = int(input())
    p = map(int, raw_input().split())
    ans = max(p)
    for cnt in xrange(2, max(p)):
        t = 0
        for x in p:
            t += (x-1)//cnt
        ans = min(ans, cnt+t)
    return ans

T = input()
for i in xrange(T):
    print 'Case #%d: %s' % (i + 1, solve())
