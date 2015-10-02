from itertools import combinations_with_replacement

questionURL = "https://www.hackerrank.com/challenges/manasa-and-stones"

numOfCases = int(raw_input())
for case in range(numOfCases):
    inputNum = [int(raw_input()) for i in range(3)]
    numOfStones, sA, sB = inputNum
    combo = combinations_with_replacement([sA, sB], numOfStones)
    print sorted(set([sum(x) for x in combo]))
