def getlength(seq):
    lens = 0
    for val in seq:
        lens += 1
        print(lens, val)


s = 'helloWorld'
print(s[-1])  # 打印最后一个字符
getlength(s)

s1 = 'abc'
s2 = 'bcd'
s3 = 'cde'
print(s3 > s2)
print(s1 > s2)
print(s1 * 3)  # 将abc复制三次

print('a' in s)
print('a' not in s)
print('W' in s)

list = [1, 2, 3, 4, 0]
print(all(list))  # 数组中的所有值均为True，则返回True，否则返回false
print(any(list))  # 只要有一个为True，则返回True，否则返回False
print(max(list))  # 返回数组中的最大值
print(min(list))  # 返回数组中的最小值

# 切片操作
print(s[0:5])  # 返回从0到5的值
print(s[0:5:2])  # 返回从0到5，步长为2的值
print(s[::2])  # 返回步长为2的值
print(s[::-1])  # 返回反向值

num = 10
print(str(num))  # 打印字符串10
list1 = [1, 2, 3, 4]
list2 = (1, 2, 3, 4)  # ()代表tuple元组数据类型,元组是一种不可变序列
print(str(list1))
print(str(list2))

c = 'a'
num = 97
print('%c' % num)
print(chr(num))         # 输出数字对应的字符
print(ord(c))           # 输出字符对应的ascii码