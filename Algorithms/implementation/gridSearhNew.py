import numpy as np
import re


def readCase():
    '''
    for each case
        first line: R, C for the grid within range (1, 1000)
        followed by R lines of C length for the gridBase

        then  r, c for pattern grid row, col (1, 1000)
        followed by r lines of c length for the gridPattern

        1<= r <=R
        1<= c <=C
    '''

    R, C = [int(i) for i in raw_input().split(" ")]
    gridBaseStr = [raw_input() for k in range(R)]
    r, c = [int(i) for i in raw_input().split(" ")]
    gridPatternStr = [raw_input() for k in range(r)]

    return R, C, gridBaseStr, r, c, gridPatternStr


def searchFunRe(R, C, gridBase, r, c, gridPattern):
    gridBaseOneLine = "".join(gridBase)

    interval = r'\S' * (C - c)
    pattern = re.compile(interval.join(gridPattern))

    match = pattern.finditer(gridBaseOneLine)

    if match:
        for m in match:
            if m.start() % C + c <= C:
                return "YES"
        return "NO"
    else:
        return "NO"


def search():
    numTestCases = int(raw_input())
    for caseNum in range(numTestCases):
        R, C, gridBase, r, c, gridPattern = readCase()
        print searchFunRe(R, C, gridBase, r, c, gridPattern)


def readFile():
    with open('input0504.txt', 'r') as f:
        numofCases = int(f.readline())
        for i in range(numofCases):
            R, C = [int(i) for i in f.readline().split(" ")]
            gridBase = [f.readline().rstrip() for k in range(R)]
            r, c = [int(i) for i in f.readline().split(" ")]
            gridPattern = [f.readline().rstrip() for k in range(r)]

            print searchFunRe(R, C, gridBase, r, c, gridPattern)

readFile()
