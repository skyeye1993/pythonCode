# 匿名方法

f1 = lambda: 10  # 无参函数，返回10
print(f1())

f2 = lambda x: x % 2 == 1  # 一个参数x  返回x%2==1的值
print(f2(5))

f3 = lambda x, y: x ** 2 - y ** 2
print(f3(5, 4))

f4 = lambda x, y, *args: x + y + sum(args)
print(f4(1, 2, 3, 4, 5, 6, 7))

f5 = lambda x, y, **kwargs: x + y + sum(list(kwargs.values()))
print(f5(1, 2, m=3, n=4))

pay = lambda time, money: (int(time / 3600) + int(time % 3600 != 0)) * money
paydis = lambda time, money, discount: pay(time, money) * discount
payfree = lambda time: 0
paykeys = ['pay', 'paydis', 'payfree']
funlist = [pay, paydis, payfree]
payd = dict(zip(paykeys, funlist))
print(payd['pay'](123, 2))

funlist = [lambda x, i1=i: x ** i1 for i in range(1, 10)]
print(funlist[0](2))
