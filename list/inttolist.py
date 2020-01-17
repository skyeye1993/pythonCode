listt = [1, 2, 3]
listt.append(4)
listt.append([6, 7, 8])
print(listt)

def inttolist(num):
    listn = []
    while num != 0:
        listn.insert(0, num % 10)  # 在0位置插入数据
        num = int(num / 10)
    return listn


print(inttolist(567189))
