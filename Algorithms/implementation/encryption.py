questionURL = "https://www.hackerrank.com/challenges/encryption"


def getRowColumn(length):
    assert isinstance(length, int)
    lowerBound = int(length**0.5)
    if lowerBound ** 2 == length:
        return lowerBound, lowerBound
    elif lowerBound * (lowerBound + 1) > length:
        row = lowerBound
        col = row + 1
        return row, col
    else:
        return lowerBound+1, lowerBound+1

msg = "chillout"
length = len(msg)
row, col = getRowColumn(length)
msgFilled = msg + " " * (row * col - length)

encryptedMsg = ["".join([msgFilled[c * col + k]
                         for c in range(row)
                         if msgFilled[c * col + k] != " "])
                for k in range(col)]

print " ".join(encryptedMsg)
