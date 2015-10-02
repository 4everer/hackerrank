questionURL = "https://www.hackerrank.com/challenges/angry-professor"

numTestCases = int(raw_input())

for i in range(numTestCases):
    numStudents, numMinimal = [int(k) for k in raw_input().split()]
    arrivalTime = [int(t) for t in raw_input().split() if int(t) <= 0]
    if len(arrivalTime) >= numMinimal:
        print "NO"  # more student come before class start, not cancelled
    else:
        print "YES"
