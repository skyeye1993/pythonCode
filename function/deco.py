# 装饰器
def cmpByscore(info):
    return float(info[1])


def cmpByLens(info):
    return int(info[2])


def cmpByCom(info):
    return int(info[3])


def parseFile(func):
    print('call parseFile')

    def sorefunc(fname):
        f = open(fname,encoding='utf-8-sig')
        minfo = list(map(lambda line: line.strip().split(), f.readlines()))
        func(minfo)
        f.close()

    return sorefunc


# sortBysocre = parseFile(sortBysocre)
@parseFile
def sortBysocre(minfo):
    minfo.sort(key=cmpByscore, reverse=True)
    print(minfo)


@parseFile
def sortByLens(minfo):
    minfo.sort(key=cmpByLens, reverse=True)
    print(minfo)


@parseFile
def sortByCom(minfo):
    minfo.sort(key=cmpByCom, reverse=True)
    print(minfo)


# sortBysocre = parseFile(sortBysocre)
# sortByLens = parseFile(sortByLens)
# sortByCom = parseFile(sortByCom)
fpath = r'D:\important\pythonCode\function\moviePlay.txt'
sortBysocre(fpath)
# sortByLens(fpath)
# sortByCom(fpath)
