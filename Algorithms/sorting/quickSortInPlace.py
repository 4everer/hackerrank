# Enter your code here. Read input from STDIN. Print output to STDOUT


def quickSortInplace(ar, l):
    # implementing quick sort with Lomuto Partitioning
    def quickSort(ar, low, high):
        if low < high:
            p = partition(ar, low, high)
            quickSort(ar, low, p - 1)
            quickSort(ar, p + 1, high)

    def partition(ar, low, high):
        pivot = ar[high]
        i = low  # place for swapping
        for j in xrange(low, high):
            if ar[j] <= pivot:
                ar[j], ar[i] = ar[i], ar[j]
                i += 1
        ar[i], ar[high] = ar[high], ar[i]
        printAr(ar)
        return i
    if l is None:
        l = len(ar)
    quickSort(ar, 0, l - 1)


def printAr(ar):
    print " ".join([str(x) for x in ar])


def readAndCall():
    length = int(raw_input())
    ar = [x for x in raw_input().split(" ")]
    quickSortInplace(ar, length)


def test():
    length = 100
    inputStr = "406 157 415 318 472 46 252 187 364 481 450 90 390 35 452 74 196 312 142 160 143 220 483 392 443 488 79 234 68 150 356 496 69 88 177 12 288 120 222 270 441 422 103 321 65 316 448 331 117 183 184 128 323 141 467 31 172 48 95 359 239 209 398 99 440 171 86 233 293 162 121 61 317 52 54 273 30 226 421 64 204 444 418 275 263 108 10 149 497 20 97 136 139 200 266 238 493 22 17 39"
    ar = [int(x) for x in inputStr.split(" ")]
    quickSortInplace(ar, length)
    # print ar
