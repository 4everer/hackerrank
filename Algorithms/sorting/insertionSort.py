#!/bin/python


def findNum(num, start, end, lst):
    mid = (start + end) / 2
    midNum = lst[mid]
    if midNum == num:
        return mid
    elif end - start <= 1:
        if lst[start] < num:
            return start + 1
        else:
            return start
    elif midNum > num:
        return findNum(num, start, mid, lst)
    elif midNum < num:
        return findNum(num, mid, end, lst)


def insertN(left, right):
    if right == []:
        return left
    else:
        num = right[0]
        newRight = right[1:]
        index = findNum(num, 0, len(left), left)
        newLeft = left[:index] + [num] + left[index:]
        return insertN(newLeft, newRight)


def insertSort(ar):
    left = [ar[0]]
    right = ar[1:]
    return insertN(left, right)

if __name__ == "__main__":
    lst = [1, 0, 3, 4, 5, -1]
    print insertSort(lst)
