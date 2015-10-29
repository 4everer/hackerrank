from itertools import combinations
from collections import defaultdict, Counter


questionURL = "https://www.hackerrank.com/challenges/sherlock-and-anagrams"


def onlineSubmission():
    numCases = int(raw_input())
    for case in range(numCases):
        string = raw_input()
        print numAnagramPair(string)


def allSubString(string):
    length = len(string)
    subString = [string[a:b]
                 for a, b in combinations(range(length + 1), 2) if a != b]
    return subString


def numAnagramPair(string):
    # count all nangrame pair
    anaPairAcc = 0
    subString = allSubString(string)
    subStringLengthOne = [s for s in subString if len(s) == 1]
    subStringRestExceptOriginal = [
        s for s in subString if len(s) != 1 and len(s) != len(string)]

    # for signle letters
    cSingle = Counter(subStringLengthOne)
    [word for word, count in cSingle.iteritems() if count > 1]
    anaPairAcc += sum([n * (n - 1) / 2 for n in cSingle.values()])

    # for other subStrings
    cOther = Counter(subStringRestExceptOriginal)
    cOther.update([s[::-1]
                   for s in subStringRestExceptOriginal
                   if s != s[::-1]])
    cOtherValidAna = [n * (n - 1) / 2
                      for w, n in cOther.iteritems() if s == s[::-1]]
    anaPairAcc += sum(cOtherValidAna)
    anaPairAcc += sum([n * (n - 1) / 2 for n in cOther.values()]) / 2

    return anaPairAcc


def numPossibleAnaPair(string):
    # count all pairs have same letters and can make anagram
    dic = defaultdict(int)
    for s in allSubString(string):
        dic[tuple(sorted(s))] += 1
    return sum(map(lambda x: x*(x-1)/2, dic.values()))


def test():
    testString = ["ifailuhkqq", "hucpoltgty",
                  "ovarjsnrbf", "pvmupwjjjf", "iwwhrlkpek", "wwjkww"]
    for string in testString:
        result = numAnagramPair(string)
        print result
        print numPossibleAnaPair(string)
        print "======================="
    #     if result != answer:
    #         "test failed at {0}, giving answer {1}".format(string, result)
    #         break
    # else:
    #     print "all test succeed"

if __name__ == "__main__":
    test()
