# Problem Description: https://code.google.com/codejam/contest/6224486/dashboard#s=p0

def solve():
    num, shy = raw_input().split()
    num = int(num)
    friends = 0
    stand = int(shy[0])
    for i in xrange(1, num + 1):
        # make sure current standing people are enough to make shy[i] stand up, 
        # if not, add friends
        if i > stand:
            friends += i-stand
            stand += i-stand
        stand += int(shy[i])
    return friends

T = input()
for i in xrange(T):
    print 'Case #%d: %s' % (i + 1, solve())
