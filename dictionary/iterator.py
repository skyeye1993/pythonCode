# 迭代器
for i in iter('asdfghjkl'):
    print(i)

# 生成器:所有的数据不是马上生产出来，生成器采用延迟机制，内存使用更加有效
gen = (i for i in range(10))
print(type(gen))
