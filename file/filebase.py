"""
    r  只读方式打开文件   文件必须存在
    w  只写方式打开文件   文件存在清空文件内容，文件不存在创建文件
    a  追加方式打开文件   文件不存在创建文件
    r+/w+  读写方式打开
    a+ 追加和读写方式打开   文件写位置位到文件尾
    rb wb ab rb+ wb+ ab+ 二进制方式打开文件，如图片

"""

path = 'D:\\student.txt'
f = open(path, 'r')
# help(f.readline)
# print(f.read())
print(f.readline())
for v in f.readlines():
    print(v.strip())
f.close()

# path = 'D:\\student1.txt'
# f = open(path, 'w')
# f.write('this is w test')
# f.close()
#
# path = 'D:\\student2.txt'
# f = open(path, 'w')
# f.write('this is w test')
# f.close()
#
# path = 'D:\\student3.txt'  # 文件必须存在
# f = open(path, 'r+')
# f.write('this is r+ test')
# f.close()
#
# path = 'D:\\student4.txt'
# f = open(path, 'w+')
# f.write('this is w+ test')
# f.close()
#
# path = 'D:\\student5.txt'
# f = open(path, 'a+')
# f.write('this is a test')
# print(f.read())          # 如果读取文件的方式是a，则此处会报错
# f.close()

