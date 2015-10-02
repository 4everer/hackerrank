import numpy as np
import re

questionURL = "https://www.hackerrank.com/challenges/the-grid-search"


def readCase(matrix=True):
    '''
    for each case
        first line: R, C for the grid within range (1, 1000)
        followed by R lines of C length for the gridBase

        then  r, c for pattern grid row, col (1, 1000)
        followed by r lines of c length for the gridPattern

        1<= r <=R
        1<= c <=C
    '''

    if matrix:
        R, C = [int(i) for i in raw_input().split(" ")]
        gridBaseStr = [" ".join([i for i in raw_input()]) for k in range(R)]
        gridBase = np.matrix(";".join(gridBaseStr))
        # print gridBase
        r, c = [int(i) for i in raw_input().split(" ")]
        gridPatternStr = [" ".join([i for i in raw_input()]) for k in range(r)]
        gridPattern = np.matrix(";".join(gridPatternStr))
        # print gridPattern
        return R, C, gridBase, r, c, gridPattern
    else:
        R, C = [int(i) for i in raw_input().split(" ")]
        gridBaseStr = [raw_input() for k in range(R)]
        r, c = [int(i) for i in raw_input().split(" ")]
        gridPatternStr = [raw_input() for k in range(r)]

        return R, C, gridBaseStr, r, c, gridPatternStr


def generateAllSubMatrix(matrix, r, c):
    matrixPool = []
    for i in range(matrix.shape[0] - r + 1):
        matrixPool += [matrix[i:i + r, j:j + c]
                       for j in range(matrix.shape[1] - c + 1)]
    return matrixPool


def patternInThePool(matrix, r, c, pattern):
    p00 = pattern[0, 0]

    for i in range(matrix.shape[0] - r + 1):
        matrixSubPool = [matrix[i:i + r, j:j + c]
                         for j in range(matrix.shape[1] - c + 1)
                         if matrix[i, j] == p00]
        for mat in matrixSubPool:
            if np.array_equal(mat, pattern):
                return "YES"
        else:
            continue
    return "NO"


def patternInThePool2(R, C, matrix, r, c, pattern):
    p00 = pattern[0, 0]
    locArr = np.where(matrix == p00)
    potentialPoolLoc = [(locArr[0][0, i], locArr[1][0, i])
                        for i in range(locArr[0].shape[1])]
    poolLoc = filter(lambda x: x[0] + r < R and x[1] + c < C, potentialPoolLoc)

    for loc in poolLoc:
        mat = matrix[loc[0]:loc[0] + r, loc[1]:loc[1] + c]
        if np.array_equal(mat, pattern):
            return "YES"
        else:
            continue
    return "NO"


def search1():
    numTestCases = int(raw_input())
    for caseNum in range(numTestCases):
        R, C, gridBase, r, c, gridPattern = readCase()
        matrixPool = generateAllSubMatrix(gridBase, r, c)
        for mat in matrixPool:
            if np.array_equal(mat, gridPattern):
                print "YES"
                break
        else:
            print "NO"


def search2():
    numTestCases = int(raw_input())
    for caseNum in range(numTestCases):
        R, C, gridBase, r, c, gridPattern = readCase()
        print patternInThePool(gridBase, r, c, gridPattern)


def search3():
    numTestCases = int(raw_input())
    for caseNum in range(numTestCases):
        R, C, gridBase, r, c, gridPattern = readCase()
        print patternInThePool2(R, C, gridBase, r, c, gridPattern)


def searchFun4(R, C, gridBase, r, c, gridPattern):
    rowNum = 0
    while rowNum < R - r:
        # print rowNum, R-r
        rowString = gridBase[rowNum]
        loc = rowString.find(gridPattern[0])
        if loc != -1:
            for i in range(1, r):
                if gridBase[rowNum + i][loc:loc + c] != gridPattern[i]:
                    break
            else:
                return "YES"
        rowNum += 1
    return "NO"


def searchFunRe(R, C, gridBase, r, c, gridPattern):
    rowNum = 0
    while rowNum < R - r:
        rowString = gridBase[rowNum]
        locLst = [m.start() for m in re.finditer(gridPattern[0], rowString)]
        if not locLst:
            for loc in locLst:
                for i in range(1, r):
                    if gridBase[rowNum + i][loc:loc + c] != gridPattern[i]:
                        break
                else:
                    return "YES"
        rowNum += 1
    return "NO"


def search4():
    def searchFunRealRe(R, C, gridBase, r, c, gridPattern):
        gridBaseOneLine = "".join(gridBase)
        interval = r'\S' * (C - c)
        pattern = re.compile(interval.join(gridPattern))
        print pattern.pattern
        m = re.search(pattern, gridBaseOneLine)
        if m is not None and m.start() % C + c <= C:
            return "YES"
        else:
            return "NO"

    numTestCases = int(raw_input())
    for caseNum in range(numTestCases):
        R, C, gridBase, r, c, gridPattern = readCase(False)
        print searchFun4(R, C, gridBase, r, c, gridPattern)

    # numTestCases = int(raw_input())
    R, C, r, c = [10, 10, 3, 4]
    grid = ["7283455864", "6731158619", "8988242643", "3830589324",
            "2229505813", "5633845374", "6473530293", "7053106601",
            "0834282956", "4607924137"]
    search = ["9505", "3845", "3530"]

    print searchFunRealRe(R, C, grid, r, c, search)
