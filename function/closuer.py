# 闭包
def getFunByn(n):
    def str2intN(strn):
        return int(strn, n)

    return str2intN


str2int2 = getFunByn(2)  # 二进制
str2int10 = getFunByn(10)  # 十进制
str2int16 = getFunByn(16)  # 十六进制

print(str2int2('10'))
print(str2int10('10'))
print(str2int16('10'))
