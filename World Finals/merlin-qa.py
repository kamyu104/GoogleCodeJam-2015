from itertools import permutations

def f(spells):
    score = 0
    for spell in spells:
        h, v = 0, 0
        for cost in spell:
            v += cost
            h = max(h, v)
        score += h
    return score


def merlin_qa(N, M, spells):
    spells = [i for i in spells if max(i) > 0]
    if not spells:
        return 0
    largest = 0
    for permutation in permutations(xrange(M)):
        val = f([[spell[i] for i in permutation] for spell in spells])
        largest = max(largest, val)
    return largest

for case in xrange(input()):
    N, M = map(int, raw_input().strip().split())
    spells = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    print "Case #%d: %d" % (case+1, merlin_qa(N, M, spells))

