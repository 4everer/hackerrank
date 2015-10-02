from itertools import combinations


def calScore(p1, p2):
    return (p1 | p2).count("1")

numPeople, numQ = [int(i) for i in raw_input().split()]
peopleLst = [bin(int(raw_input(), 2)) for p in xrange(numPeople)]

score = {i: [] for i in range(numQ + 1)}

for p1, p2 in combinations(peopleLst, 2):
    score[calScore(p1, p2)].append((p1, p2))

for i in range(0, numQ):
    if score[numQ - i]:
        print numQ - i
        print len(score[numQ - i])
        break
