def fun1():
    pass
print(fun1())

def fun2():
    return 1, 2, 3
print(fun2())
x, y, z = fun2()
print(x, y, z)

def foo1(x, y=2):  # 默认y为2
    return x / y
print(foo1(10))
print(foo1(10, 5))

def foo2(x,y):
    return x*y
print(foo2(y=3,x=5))  #顺序可以调换

#*arg表示可变参数
def fun3(x,y,*arg):   #一个*表示元祖
    print(x,y,arg)
fun3(1,2,3,4)
fun3(1,2)

t = (10,20)
print(*t)

#**arg 表示字典
def fun4(x,y,**arg):
    print(x,y,arg)
fun4(1,2)
fun4(1,2,m=1,n=2)