t1 = (1)
print(type(t1))
t2 = (1,)
print(type(t2))
t3 = tuple('123')
print(t3)
print(id(t3))
t3 = ('0',) + t3
print(id(t3))  # 与上一个id是不一致的
print(t3)

print(t3.count('0'))
print(t3.index('2'))

t4 = [0, '123', [1, 2, 3]]   # 列表中的数据类型是不可变的，但列表内的元素可以变
t4[2][0] = 0
print(t4)
