def mycount(str, subs):
    length = len(subs)
    index = 0
    num = 0
    for i in range(0, len(str)):
        tmp = str[i: i + length]
        if subs == tmp:
            num += 1
        index += 1
    return num


str1 = 'aabbcdefefefefe'
print(mycount(str1, 'ef'))
