def listtostr(list):
    result = ''
    """
        for i in list:
        result += str(i)
        return result
    """
    result = str(list).strip('[]').replace(', ', '')   # 去除头尾在 [] 中出现的字符
    result = str(list)[1:-1].replace(', ', '')   # 1第一个位置   -1最后一个位置
    return result


list1 = [1, 2, 3, 4, 5]
print(listtostr(list1))
