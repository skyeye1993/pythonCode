import random

listnum = [str(val) for val in range(1, 5)]
print(listnum)
print([int(val) for val in listnum])
print(list(map(int, listnum)))


def fun_add(x, y, z):
    return int(x) + int(y) + int(z)


gen = lambda len: [str(random.randrange(30, 100)) for val in range(len)]
list1 = gen(4)
list2 = gen(4)
list3 = gen(4)
print(list1, list2, list3)
print(list(map(fun_add, list1, list2, list3)))
print(list(map(lambda *args: args, list1, list2, list3)))
print(list(map(lambda *args: sum([int(val) for val in args]), list1, list2, list3)))
print(list(map(lambda *args: sum(map(int, args)), list1, list2, list3)))

fpath = 'D:\\important\\pythonCode\\function\\moviePlay.txt'
f = open(fpath,encoding='UTF-8-sig')
result = map(lambda line: line.strip().split()[:2], f.readlines())
result = list(result)
result.sort(key=lambda vals: vals[1])
for val in result:
    print(val)

listn1 = [1, 2, 3]
listn2 = [1, 2]
print(list(map(lambda x, y: x + y, listn1, listn2)))