from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    aList = a.split("\n")
    bList = b.split("\n")
    commonList = []
    # check if lines of a is in b
    for aElement in aList:
        if aElement in bList and aElement not in commonList:
            commonList.append(aElement)
    return commonList


def sentences(a, b):
    """Return sentences in both a and b"""
    aList = sent_tokenize(a)
    bList = sent_tokenize(b)
    commonList = []
    # check if sentences of a is in b
    for aElement in aList:
        if aElement in bList and aElement not in commonList:
            commonList.append(aElement)
    return commonList


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    aList = []
    bList = []
    commonList = []
    for i in range(len(a) - n + 1):
        if a[i:i+n] not in aList:
            aList.append(a[i:i+n])
    for i in range(len(b) - n + 1):
        if b[i:i+n] not in bList:
            bList.append(b[i:i+n])
    # check if substrings of a is in b
    for aElement in aList:
        if aElement in bList and aElement not in commonList:
            commonList.append(aElement)
    return commonList
