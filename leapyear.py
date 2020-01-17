year = 2004
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print('leapyear')
else:
    print('not leapyear')

for year in range(1900, 2020, 4):  # 从1900年到2019年（不包括2020） 步进为4
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(year)

print('-------------------------------------------')
'''函数'''


def isleayear(year1):
    if year1 % 400 == 0 or year1 % 4 == 0 and year1 % 100 != 0:
        print('leapyear')
        return True
    else:
        print('not leapyear')
        return False


print(isleayear(2003))
