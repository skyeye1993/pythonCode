listl = ['', 0, 1, 2, []]
print([val for val in listl if val])
print(list(filter(None, listl)))


def isEven(val):
    return val % 2 == 0


result = filter(isEven, range(0, 20))
print(list(result))
result = filter(lambda val: val % 2 == 0, range(0, 20))
print(list(result))


def mycmp(val):
    print('call filter')
    return int(val[2]) > 60

path = r'D:\important\pythonCode\function\math.txt'
f = open(path)
minfo = map(lambda line: line.strip().split(), f.readlines())
minfo = list(minfo)
print(minfo)
mpass = filter(mycmp,minfo)
print('run filter')
print(list(mpass))