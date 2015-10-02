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


def readFile():
    with open('input0504.txt', 'r') as f:
        numofCases = int(f.readline())
        for i in range(numofCases):
            R, C = [int(i) for i in f.readline().split(" ")]
            gridBase = [f.readline().rstrip() for k in range(R)]
            r, c = [int(i) for i in f.readline().split(" ")]
            gridPattern = [f.readline().rstrip() for k in range(r)]
            print searchFun4(R, C, gridBase, r, c, gridPattern)
