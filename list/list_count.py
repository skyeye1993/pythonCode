list1 = [1, 2, 3, 4, 5, 6]
print(list1.count(1))
print(list1.index(1))  # 返回1出现的第一个位置，如果不返回则报异常


def myfind(listn, val):
    """
    查找与list中相同的val值的位置，如果相同返回当前地址，否则返回-1
    """
    for index, tmp in enumerate(listn):
        if val == tmp:
            return index
    return -1


def binarySearch(listn, val):
    start = 0
    end = len(listn) - 1
    while start < end:
        mid = int((start + end) / 2)
        if listn[mid] == val:
            return mid
        elif listn[mid] > val:
            end = mid
        else:
            start = mid
    return -1


print(myfind(list1, 10))
print(binarySearch(list1, 1))
