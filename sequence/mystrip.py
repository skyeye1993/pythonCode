def mystrip(src, chars=' '):
    s_index = 0
    e_index = len(src)
    for i in src:
        if chars.find(i) == -1:
            break
        s_index += 1
    for i in src[::-1]:  # 从后往前
        if chars.find(i) == -1:
            break
        e_index -= 1
    return src[s_index:e_index]


print(mystrip('   aaacasdf   '))  # 如果不加chars参数，则由mystrip函数定义，默认为 ' '
print(mystrip('123asdfcdf56798', '1234567890'))
