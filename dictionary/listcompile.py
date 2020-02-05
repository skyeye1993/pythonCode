# 列表解析

keys = [chr(val) for val in range(ord('a'), ord('z') + 1)]
print(keys)

import random

nums = [random.randint(1, 100) for i in range(10)]
print(nums)

num = 234
strs = [int(c) for c in str(num)]
print(strs)

listnum = [random.randint(0, 100) for i in range(10)]
listnum = [num for num in listnum if num > 60]
print(listnum)

binfo = 'book,python,25,zhang,,-,1231'
listr = binfo.split(',')
print(listr)
listr = [s for s in listr if len(s.strip()) > 1]
print(listr)

list1 = [[val] for val in range(3)]
print(list1)

list2 = [[x, y, z] for x in range(3) if x % 2 == 0 for y in range(3) if y % 2 for z in range(3)]
print(list2)

#生成水仙花数
print([num for num in range(100, 1000) if sum([int(n) ** len(str(num)) for n in str(num)]) == num])
