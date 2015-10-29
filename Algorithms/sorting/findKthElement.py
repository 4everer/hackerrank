def find_kth(ar, k):
    pivot = ar[0]
    left, right = split(ar[1:], pivot)
    if k == len(left):
        return pivot
    elif k < len(left):
        return find_kth(left, k)
    elif k > len(left):
        return find_kth(right, k - len(left) - 1)


def split(ar, k):
    # left + [k] + right
    left = []
    right = []
    for i in ar:
        if i <= k:
            left.append(i)
        elif i > k:
            right.append(i)
    return left, right


lst = [1, 2, 3, 4, 5]
length = len(lst)
print find_kth(lst, (length-1)/2)
