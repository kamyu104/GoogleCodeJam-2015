def solve():
    num, level = raw_input().split()
    num = int(num)
    ans = 0
    cur = int(level[0])
    for i in xrange(1, num + 1):
        if i > cur:
            ans += i-cur
            cur += i-cur
        cur += int(level[i])
    return ans

T = input()
for i in xrange(T):
    print 'Case #%d: %s' % (i + 1, solve())
