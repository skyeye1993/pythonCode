x1 = 10
def fun1(x1):
    print(locals())
    x1 = 20
print(globals())
fun1(x1)
print(x1)

x2 = 10
def fun2():
    global x2
    x2 = 20
fun2()
print(x2)

ltest1=[]
def fun3(l):
    l.append(1)
fun3(ltest1)
print(ltest1)

ltest2=[]
def fun4(l):
    l = [100]    #重新指向了另外一个数组[100]
fun4(ltest2)
print(ltest2)