# 求5的阶乘
n = 5
val = 1
while n > 0:
    val *= n
    n -= 1
print(val)

from functools import reduce

n = 5
print(reduce(lambda x, y: x * y, range(1, n + 1)))


def recur(n):
    if n <= 1:
        return 1
    else:
        return n * recur(n - 1)


print(recur(5))

listn = [1, 2, [3, 4, [5, 6, [7]]]]


def func_l(listm):
    for val in listm:
        if isinstance(val, list):
            func_l(val)
        else:
            print(val)


func_l(listn)


def fab(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)


print(fab(10))

listfab = [1, 1]
for i in range(2, 11):
    listfab.append(listfab[i - 1] + listfab[i - 2])
print(listfab)
