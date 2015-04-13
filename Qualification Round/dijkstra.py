def mul(a, b, sign):
    if a == 'i':
        if b == 'i':
            return '1', sign * -1
        elif b == 'j':
            return 'k', sign
        elif b == 'k':
            return 'j', sign * -1
    elif a == 'j':
        if b == 'i':
            return 'k', sign * -1
        elif b == 'j':
            return '1', sign * -1
        elif b == 'k':
            return 'i', sign
    elif a == 'k':
        if b == 'i':
            return 'j', sign 
        elif b == 'j':
            return 'i', sign * -1
        elif b == 'k':
            return '1', sign * -1
    else:
        return b, sign

def solve():
    l, rep = map(int, raw_input().split())
    s = raw_input()

    # every four copies of anything mutilply to 1, so we can reduce mod 4
    # at most we need 4 copies in each of the first two splits (4 for i, rep % 4 for j, 4 for k).
    if rep >= 8:
        rep = 4 + rep % 4 + 4

    s *= rep

    status, p, sign  = 0, '1', 1
    for q in s:
        p, sign = mul(p, q, sign)
        if status == 0 and p == 'i' and sign == 1:
            status = 1
        elif status == 1 and p == 'k' and sign == 1:
            status = 2

    if status == 2 and p == '1' and sign == -1:
        return "YES"
    else:
        return "NO"

T = input()
for i in xrange(T):
    print 'Case #%d: %s' % (i + 1, solve())
