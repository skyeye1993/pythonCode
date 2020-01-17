import random


def generate(list, num):
    for i in range(0, num):
        list.append(random.randint(0, 10))


def removesame(list):
    dellist = []
    for val in list:
        n = list.count(val)
        if n > 1 and n not in dellist:
            dellist.append(val)
    for delval in dellist:
        n = list.count(delval)
        while n > 1:
            list.remove(delval)
            n -= 1


list = []
generate(list, 10)
print(list)
removesame(list)
print(list)
