"""
文件指针

SEEK_SET = 0  表示文件指针的文件头位置位置
SEEK_CUR = 1  表示文件指针的当前位置
SEEK_END = 2  表示文件指针的文件尾位置

"""
import os

# f = open('D:\\seek.txt', 'r')
# print(f.tell())  # 获取文件指针的当前位置
# print(f.read(2))  # 获取文件的前两个字符，文件指针位置会到2
# f.seek(5)  # 将文件指针位置定位到5
# print(f.read())
# f.seek(1, os.SEEK_SET)  # 从os.SEEK_SET的位置向后偏移一个位置
# print(f.read())
# f.seek(-1, os.SEEK_END)  # 此处会报错（如果想不报错，那么需要使用二进制读取方式）

f = open('D:\\seek.txt', 'rb+')
f.seek(-1, os.SEEK_END)
print(f.read())
f.seek(2, os.SEEK_SET)
f.write(b'1')  # 写二进制的'1'
