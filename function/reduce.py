from functools import reduce

listnum = [val for val in range(1, 5)]
print(listnum)
print(sum(listnum))
print(reduce(lambda x, y: x + y, listnum))

liststr = [str(val) for val in listnum]
print(liststr)
print(reduce(lambda x, y: x + y, liststr))
print(reduce(lambda x, y: x*10 + y, map(int,liststr)))


def func(result, info):
    info = list(map(float, info))
    result += reduce(lambda x, y: x*y, info)

    return result

fpath = r'F:\workdir\func\order.txt'
f = open(fpath)
mlist = map(lambda line:line.strip().split()[1:], f.readlines())
result = reduce(lambda tmp, info: tmp + reduce(lambda x, y: x*y,map(float, info)), mlist, 0)
print (result)
