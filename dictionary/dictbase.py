# 字典：就是java中的对象转换成json
d1 = {'name': 'zhangsan', 'age': 12, 'weight': 101}
print(d1)
print(d1['name'])

d2 = dict(a=1, b=2)
print(d2)

d3 = dict((('ip', '127.0.0.1'), ('port', 8080)))
print(d3)

d4 = dict.fromkeys('abcd', -1)
print(d4)

# 能当key的类型：数字，字符串，元组（不可变字符序列）
d5 = {'port': 8080, 'port': 80}
print(d5)

d6 = {1: '1', 1.0: '1.0'}
print(d6)
print('id(1)=' + str(hash(1)), 'id(1.0)=' + str(hash(1.0)))  # 1.0和1的hash值是相同的，所以会把前一个value给覆盖掉

for k in d1.keys():  # 获取key
    print(d1[k])
for v in d1.values():  # 获取val
    print(v)
for k, v in d1.items():  # 获取key和value
    print(k, v)

d = {'weight': 100}
d1.update(d)  # 将一个字典中的值更新到另一个字典中
print(d1)
d1.setdefault('height', 170)
print(d1)

print(d1.popitem())
print(d1)
