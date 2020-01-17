listn = [1, 3, 5, 2, 3, 8, 6]
listn.sort(reverse=True)
print(listn)

lists = ['java', 'c++', 'python', 'scala', 'verilog']
lists.sort()
print(lists)
lists.sort(key=len)
print(lists)


def getSecond(list):
    return -list[1]


listl = [[60, 80, 100], [70, 70, 70], [80, 10, 10]]
listl.sort()
print(listl)
listl.sort(key=sum)
print(listl)
listl.sort(key=getSecond)  # 以每个数组中第二个数字逆序排序
print(listl)
