def getFlower(start, end):
    l = []
    for val in range(start, end):
        tmp = str(val)
        n = len(tmp)
        count = 0
        for v in tmp:
            count += int(v) ** n
        if count == val:
            l.append(val)
    return l


print(getFlower(100, 10000))
