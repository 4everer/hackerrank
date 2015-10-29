questionURL = "https://www.hackerrank.com/challenges/bigger-is-greater"


def onlineSubmission():
    numCases = int(raw_input())
    for case in range(numCases):
        print findNextWord(raw_input())


def findNextWord(word):
    '''
        using letters in original word, find next word in lexicographical
        order
    '''
    wordLst = [s for s in word]
    tail = [wordLst.pop()]
    while wordLst:
        t = wordLst.pop()
        if ord(tail[-1]) > ord(t):
            firstLagerThan_t = [
                n for n, l in enumerate(tail) if ord(l) > ord(t)][0]
            tailNew = tail[:firstLagerThan_t] + [t] + tail[firstLagerThan_t+1:]
            return "".join(wordLst) + tail[firstLagerThan_t] + "".join(tailNew)
        else:
            tail.append(t)
    return "no answer"


def test():
    testWord = ["ab", "bb", "hefg", "dhck", "abcedd", "dkhc"]
    answer = ["ba", "no answer", "hegf", "dhkc", "abdcde", "hcdk"]
    # for word in testWord:
    #     print findNextWord(word)
    for i in range(len(testWord)):
        if findNextWord(testWord[i]) != answer[i]:
            print testWord[i] + "failed"
            break
    else:
        print "test succeed"


if __name__ == "__main__":
    test()
