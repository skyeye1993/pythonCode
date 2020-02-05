"""
    统计一个文件中单词出现的个数
"""

def fileread(path):
    result = 0
    f = open(path, 'r+')
    for line in f:
        word = [word for word in line.strip().split(' ') if word.strip()]
        result += len(word)
    return result


path = 'D:\\student.txt'
result = fileread(path)
print(result)
