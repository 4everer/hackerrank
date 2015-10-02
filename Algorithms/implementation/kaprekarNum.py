questionURL = "https://www.hackerrank.com/challenges/kaprekar-numbers"

#lowBound = int(raw_input())
#upperBound = int(raw_input())

def ifKaprekar(n):
    n2 = n**2
    n2Str = str(n2)
    lN2 = len(n2Str)

    if lN2 == 1 and n in [1, 9]:
        return True
    if lN2 > 1:
        if lN2 % 2 == 0:
            leftNum = n2Str[0:lN2/2]
            rightNum = n2Str[lN2/2:lN2]
            return int(leftNum) + int(rightNum) == n
        elif lN2 % 2 == 1:
            leftNum = n2Str[0:lN2/2]
            rightNum = n2Str[lN2/2:lN2]
            return int(leftNum) + int(rightNum) == n
        else:
            return False


kaprekar = [str(k) for k in range(1, 99999+1) if ifKaprekar(k)]
if len(kaprekar) > 0:
    print " ".join(kaprekar)
else:
    print "INVALID RANGE"
