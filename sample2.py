score = 80
passline1 = 160
'''
这是注释
'''
"""
这是注释
"""
if score > passline1:
    print("pass")
else:
    print("not pass")

x, y, z = 10, 20, 30
print("x=%d\ny=%d\nz=%d" % (x, y, z))

temp1 = 'temp1'
temp2 = 'temp2'
print('%s %s' % (temp1, temp2))

pi = 3.1415926
print('%f' % pi)
print('%.7f' % pi)

print('%d%%' % x)  # 两个%表示打印%

temp3 = '%s' % 'temp3'
print('%s' % temp3)

temp4 = '%x' % 90  # 将temp赋值为16进制
print(temp4)

temp5 = '%c' % 97  # temp5为字符值为97
print(temp5)
print('0x%x' % id(temp5))

print('------------------------------')
print(4 / 3)
print(4 // 3)  # 地板除
print(1 and 2 and 3)  # 如果全部为非零则返回最后一个非零
print(1 or 2 or 3)  # 返回第一个非零
print(0 or None or 1)
print(not 0, not 1, not None, not 'sss', not x)

print('-------------------------------')
if score > 80:
    print('A')
elif score > 70:
    print('B')
else:
    print('C')

