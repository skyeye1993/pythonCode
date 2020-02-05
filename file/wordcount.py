def fileread(path):
    f = open(path, 'r+')
    dtmp = {}
    for line in f:
        words = [word for word in line.strip().split(' ') if word.strip()]
        for word in words:
            if word in dtmp:
                dtmp[word] += 1
            else:
                dtmp[word] = 1
    f.close()
    return dtmp


def wordCmp(d):
    return list(d.values())[0]


def wordcount(dwords):
    l = [dict([dw]) for dw in dwords.items()]
    print(l)
    l.sort(key=wordCmp)
    return l


path = 'D:\\student.txt'
result = fileread(path)
l = wordcount(result)
print(l[-2:])
