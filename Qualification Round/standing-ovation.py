# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Qualification Round - Problem A. Standing Ovation
# https://code.google.com/codejam/contest/6224486/dashboard#s=p0
#
# Time:  O(S)
# Space: O(1)
#

def invite():
    num, shy = raw_input().strip().split()
    num = int(num)
    friends = 0
    stand = int(shy[0])
    for i in xrange(1, num+1):
        # Make sure current standing people are enough to make shy[i] stand up, 
        # if not, add friends
        if i > stand:
            friends += i-stand
            stand += i-stand
        stand += int(shy[i])
    return friends

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, invite())
