def solve():
    [x, r, c]  = map(int, raw_input().split())
  
    if x>=7:
        #A polyomino with a monomino hole cannot be part of a tiling
        return "RICHARD"
  
    if (r*c)%x != 0:
        #The grid is not tilable by X-ominoes
        return "RICHARD"
    
    if x > max(r,c):
        #The straight X-omino does not fit in the grid
        return "RICHARD"

    if (x+1)//2 > min(r,c):
        #The most even-armed V-shaped X-omino does not fit in the grid
        # x
        # x
        # xxx
        return "RICHARD"

    if x==4 and min(r,c)==2:
         #Richard wins by picking thie S tetromino
         # xx
         #  xx
         return "RICHARD"

    if x==5 and min(r,c)==3 and max(r,c)==5:
         #Richard wins by choosing the W pentomino
         # x
         # xx
         #  xx 
         return "RICHARD"
  
    if x==6 and min(r,c)==3:
         #Richard wins by choosing the T with a length 4 top bar
         # xxxx
         #  x
         #  x
         return "RICHARD"
  
    #Gabriel can easily work around the tile in other cases
    return "GABRIEL"

T = input()
for i in xrange(T):
    print 'Case #%d: %s' % (i + 1, solve())
