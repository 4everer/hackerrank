questionURL = "https://www.hackerrank.com/challenges/sherlock-and-the-beast"

numTestCases = int(raw_input())

for i in range(numTestCases):
    digitsNum = int(raw_input())

    if digitsNum % 3 == 0:
        print "5" * digitsNum
    elif digitsNum % 3 == 1 and digitsNum >= 10:
        print "5" * (digitsNum - 10) + "3" * 10
    elif digitsNum % 3 == 2 and digitsNum >= 5:
        print "5" * (digitsNum - 5) + "3" * 5
    else:
        print "-1"
