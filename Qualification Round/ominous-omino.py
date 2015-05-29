# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Qualification Round - Problem D. Ominous Omino
# https://code.google.com/codejam/contest/6224486/dashboard#s=p3
#
# Time:  O(1)
# Space: O(1)
#

def omino():
    [X, R, C]  = map(int, raw_input().strip().split())
  
    if X>=7:
        #A polyomino with a monomino hole cannot be part of a tiling
        return "RICHARD"
  
    if (R*C)%X != 0:
        #The grid is not tilable by X-ominoes
        return "RICHARD"
    
    if X > max(R,C):
        #The straight X-omino does not fit in the grid
        return "RICHARD"

    if (X+1)//2 > min(R,C):
        #The most even-armed V-shaped X-omino does not fit in the grid
        # x
        # x
        # xxx
        return "RICHARD"

    if X==4 and min(R,C)==2:
         #Richard wins by picking thie S tetromino
         # xx
         #  xx
         return "RICHARD"

    if X==5 and min(R,C)==3 and max(R,C)==5:
         #Richard wins by choosing the W pentomino
         # x
         # xx
         #  xx 
         return "RICHARD"
  
    if X==6 and min(R,C)==3:
         #Richard wins by choosing the T with a length 4 top bar
         # xxxx
         #  x
         #  x
         return "RICHARD"
  
    #Gabriel can easily work around the tile in other cases
    return "GABRIEL"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, omino())
