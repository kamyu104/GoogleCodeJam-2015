# Problem Description: https://code.google.com/codejam/contest/6224486/dashboard#s=p1

def solve():
    d = int(input())
    p = map(int, raw_input().split())
    ans = max(p)
    
    # try to split each plate into target count of pancakes, and count waiting time
    for cnt in xrange(2, max(p)):
        wait = 0
        for x in p:
            wait += (x-1)//cnt
        ans = min(ans, cnt+wait)
    return ans

T = input()
for i in xrange(T):
    print 'Case #%d: %s' % (i + 1, solve())
