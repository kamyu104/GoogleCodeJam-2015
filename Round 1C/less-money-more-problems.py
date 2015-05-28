# https://code.google.com/codejam/contest/4244486/dashboard#s=p2
# Time:  O(V)
# Space: O(1)

def new_denominations(C, V, D, denominations):
    # First, we remove all denominations that are too big
    while D > 0 and denominations[D-1] > V:
        denominations.pop()
        D -= 1
    
    number, i, highest_reached = 0, 0, 0
    while highest_reached < V:
        # Use the old denomination of coin to extend highest_reached.
        if i < D and highest_reached + 1 >= denominations[i]:
            highest_reached += C * denominations[i]
            i += 1
        # Make a new denomination of coin to extend highest_reached.
        else:
            new_denomination = highest_reached + 1
            highest_reached += C * new_denomination
            number += 1
    
    return number

for case in xrange(input()):
    C, D, V = map(int, raw_input().strip().split())
    denominations = map(int, raw_input().strip().split())
    print "Case #{:d}: {:d}".format(case+1, new_denominations(C, V, D, denominations))
