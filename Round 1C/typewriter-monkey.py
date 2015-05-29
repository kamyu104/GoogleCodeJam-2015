# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 1C - Problem B. Typewriter Monkey
# https://code.google.com/codejam/contest/4244486/dashboard#s=p1
#
# Time:  O(K + L * S)
# Space: O(K + L)
#

def chars_before_repeat(s):
    L = len(s)
    # s = ABA, res => 2 because after 2 chars we can start a new pattern already
    for i in xrange(1, L+1):
        if s[i:] == s[0:L-i]:
            return i
    return L

def remaining_bananas(K, L, S, keyboard, target):
    if L > S:
        return 0
    
    # Compute keyboard frequency
    keyboard_freq = {}
    for k in keyboard:
        if k in keyboard_freq:
            keyboard_freq[k] += 1
        else:
            keyboard_freq[k] = 1

    # Make sure all necessary letters are there.
    for k in target:
        if k not in keyboard_freq:
            return 0
    
    # First, what is the maximum number of repeats?
    spacing = chars_before_repeat(target)
    ideal_bananas = (S-L)//spacing + 1
    
    # Second, what is the average number of repeats?
    keyboard_prob = {}
    for k,v in keyboard_freq.iteritems():
        keyboard_prob[k] = v / float(K)
    
    if L == 1:
        return ideal_bananas - S * keyboard_prob[target[0]]

    # Sum up each probability of the string at position i matching the target by DP.
    expected_bananas = 0.0
    running_prob = [0.0 for i in xrange(L-1)]
    for i in xrange(S):
        # Given i, running_prob[j] means probability of S[i-j:i+1] matching target[:j+1].
        expected_bananas += running_prob[L-2] * keyboard_prob[target[L-1]]
        
        # Update the probability in the current index i.
        for j in xrange(L-2, 0, -1):
            running_prob[j] = running_prob[j-1] * keyboard_prob[target[j]]
        running_prob[0] = keyboard_prob[target[0]]
    
    return ideal_bananas - expected_bananas

for case in xrange(input()):
    K, L, S =  map(int, raw_input().strip().split())
    keyboard = raw_input()
    target = raw_input()
    print "Case #{:d}: {:.10f}".format(case+1, remaining_bananas(K, L, S, keyboard, target))
