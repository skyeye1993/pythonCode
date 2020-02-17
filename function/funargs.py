path = 'D:\\report.txt'


def parseFile(fpath):
    f = open(fpath, 'r')
    result = {}
    for line in f:
        tmp = [val.strip(':') for val in line.strip().split()]
        d = dict(name=tmp[1], score=tmp[2])
        result[int(tmp[0])] = d
    return result


def searchbyids(data, id, *args):
    ids = list(args)
    ids.insert(0, id)
    scores = []
    for v in ids:
        scores.append(data[v]['score'])
    return dict(list(zip(ids, scores)))


def comb(x, y):
    return x > y


def coms(x, y):
    return x < y


def searchByRange(data, sid=1, eid=None, passline=None, cmpfun=comb):
    if eid == None:
        eid = len(data)
    scores = []
    for id in range(sid, eid + 1):
        scores.append(data[id]['score'])
    print(scores)
    if passline == None:
        return scores
    passscore = [val for val in scores if cmpfun(int(val), passline)]   #筛选出大于passline的数据
    print(passscore)
    return passscore


result = parseFile(path)
t = searchbyids(result, 1, 4, 12, 35)
print(t)
searchByRange(result)
searchByRange(result, passline=70)
