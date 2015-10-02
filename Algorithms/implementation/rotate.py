questionURL = "https://www.hackerrank.com/challenges/matrix-rotation-algo"


class OuterBound:

    def __init__(self, first, colOuter, last):
        self.first = first
        self.colOuter = colOuter
        self.last = last

        self.row = self.getRowNum()
        self.col = self.getColNum()

    def getRowNum(self):
        if self.colOuter:
            return 2 + len(self.colOuter[0])
        else:
            return 2

    def getColNum(self):
        return len(self.first)

    def rotate(self):
        col1, col2 = self.colOuter
        newFirst = self.first[1:] + [col2[0]]
        newLast = [col1[-1]] + self.last[:-1]
        col1 = [self.first[0]] + col1[:-1]
        col2 = col2[1:] + [self.last[-1]]
        return OuterBound(newFirst, [col1, col2], newLast)

    def rotateN(self, rotateTimes):
        equalRotate = rotateTimes % ((self.row + self.col) * 2 - 4)
        if equalRotate > 0:
            result = self.rotate()
            for i in range(equalRotate-1):
                result = result.rotate()
            return result
        else:
            return self

class Grid:

    def __init__(self, first, middle, last):

        self.first = first
        self.middle = middle
        self.last = last

        self.row = self.getRowNum()
        self.col = self.getColNum()

    def getRowNum(self):
        if self.middle:
            return 2 + len(self.middle)
        else:
            return 2

    def getColNum(self):
        return len(self.first)

    def isCoreGrid(self):
        if self.row > 2 and self.col > 2:
            return False
        else:
            return True

    def coreGridShape(self):
        if self.row == min([self.row, self.col]):
            coreRow = 2
            coreCol = 2 + self.col - self.row
        else:
            coreCol = 2
            coreRow = 2 + self.row - self.col
        return coreRow, coreCol

    def findNextInnerGrid(self):
        if not self.isCoreGrid():
            inner = Grid(self.middle[0][1:-1],
                         [self.middle[i][1:-1]
                          for i in range(1, len(self.middle) - 1)],
                         self.middle[len(self.middle) - 1][1:-1])
            return inner
        else:
            return []

    def findColOuterBound(self):
        colOuter = [[row[0] for row in self.middle],
                    [row[-1] for row in self.middle]]
        return colOuter

    def findOuterBound(self):
        return OuterBound(self.first, self.findColOuterBound(), self.last)

    def toSimpleGrid(self):
        return [self.first] + self.middle + [self.last]

    def assemble(self, first, last, colOuter, inner):
        # use first, last, colOuter, inner to assemble thr Grid
        colOuterLeft, colOuterRight = colOuter
        if inner:
            middle = [[colOuterLeft[i]] + inner.toSimpleGrid()[i] +
                      [colOuterRight[i]] for i in range(len(colOuterLeft))]
            return Grid(first, middle, last)
        else:
            middle = [[colOuterLeft[i]] +
                      [colOuterRight[i]] for i in range(len(colOuterLeft))]
            return Grid(first, middle, last)

    def rotate1(self):
        # first layer rotate
        if self.isCoreGrid():
            if self.row == 2:
                newFirst = self.first[1:] + [self.last[-1]]
                newLast = [self.first[0]] + self.last[:-1]
                return Grid(newFirst, [], newLast)
            else:
                col1, col2 = self.findColOuterBound()
                newFirst = [self.first[1], col2[0]]
                newLast = [col1[-1], self.last[0]]
                col1 = [self.first[0]] + col1[:-1]
                col2 = col2[1:] + [self.last[-1]]
                return self.assemble(newFirst, newLast, [col1, col2], [])
        else:
            col1, col2 = self.findColOuterBound()
            newFirst = self.first[1:] + [col2[0]]
            newLast = [col1[-1]] + self.last[:-1]
            col1 = [self.first[0]] + col1[:-1]
            col2 = col2[1:] + [self.last[-1]]
            return self.assemble(newFirst, newLast,
                                 [col1, col2],
                                 self.findNextInnerGrid().rotate1())

    def coreRotate(self):
        if self.row == 2:
            newFirst = self.first[1:] + [self.last[-1]]
            newLast = [self.first[0]] + self.last[:-1]
            return Grid(newFirst, [], newLast)
        else:
            col1, col2 = self.findColOuterBound()
            newFirst = [self.first[1], col2[0]]
            newLast = [col1[-1], self.last[0]]
            col1 = [self.first[0]] + col1[:-1]
            col2 = col2[1:] + [self.last[-1]]
            return self.assemble(newFirst, newLast, [col1, col2], [])

    def rotate2(self, rotateTimes):
        if self.isCoreGrid():
            equalRotate = rotateTimes % ((self.row + self.col) * 2 - 4)
            if equalRotate > 0:
                tmp = self.coreRotate()
                for i in range(equalRotate-1):
                    tmp = tmp.coreRotate()
                return tmp
            else:
                return self
        else:
            outer = self.findOuterBound()
            outer = outer.rotateN(rotateTimes)
            col1, col2 = outer.colOuter
            newFirst = outer.first
            newLast = outer.last
            return self.assemble(newFirst, newLast,
                                 [col1, col2],
                                 self.findNextInnerGrid().rotate2(rotateTimes))

    def __str__(self):
        if self.middle:
            middleStr = "\n".join([" ".join(r) for r in self.middle])
            gridStr = " ".join(self.first) + "\n" + \
                middleStr + "\n" + " ".join(self.last)
        else:
            gridStr = " ".join(self.first) + "\n" + " ".join(self.last)

        return gridStr


def readInput():
    row, col, r = [int(i) for i in raw_input().split()]
    rowFirst = raw_input().split()
    rowMiddle = [raw_input().split() for k in range(1, row - 1)]
    rowLast = raw_input().split()
    g = Grid(rowFirst, rowMiddle, rowLast)
    return g, r


def readFile(filename):
    with open(filename, 'r') as f:
        row, col, r = [int(i) for i in f.readline().split()]
        rowFirst = f.readline().split()
        rowMiddle = [f.readline().split() for k in range(1, row - 1)]
        rowLast = f.readline().split()
        g = Grid(rowFirst, rowMiddle, rowLast)
        return g, r


if __name__ == "__main__":
    test = Grid(["1", "2", "3", "4"],
                [["5", "6", "7", "8"], ["9", "10", "11", "12"]],
                ["13", "14", "15", "16"])

    print test
    print test.rotate2(10)
    print "==================="
    #print test.findNextInnerGrid().rotate2(5)
    # print test.assemble(["1", "2", "3", "4"],
    #                     ["13", "14", "15", "16"],
    # test.findColOuterBound(), test.findNextInnerGrid())

    #g, rotateTimes = readFile("input09.txt")
    #print g.rotate2(rotateTimes)
