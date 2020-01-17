import math

"""方法之间需要间隔两个空行"""


def getGrade(score):
    """
        if score > 100:
        pass
    elif score >= 90:
        print('A')
        result = 'A'
    elif score >= 75:
        print('B')
        result = 'B'
    elif score >= 60:
        print('C')
        result = 'C'
    else:
        print('D')
        result = 'D'
    return result
    """
    result = 90 <= score <= 100 and 'A' \
             or score >= 75 and 'B' \
             or score >= 60 and 'C' \
             or 'D'
    return result


print(getGrade(100))
print(getGrade(95))
print(getGrade(80))
print(getGrade(63))
print(getGrade(50))

print(int(1.5))
print('----------------------------------')
x, y, z = 10, 20, 30
print(max(x, y, z))  # 求取最大值
print(pow(x, 2))  # 求取x的平方
print(pow(x, 3))  # 求取x的三次方
print(math.sqrt(x)) # 求根号