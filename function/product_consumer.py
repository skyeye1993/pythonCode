def product(con):
    n = 0
    while n < 10:
        print('send num:', n)
        recvmsg = con.send(n)
        print('product:', recvmsg)
        n += 1


def consumer():
    msg = ''
    print('start')
    while True:
        num = yield msg
        print('consumer recv:', num)
        msg = 'consumer to product:' + str(num)


con = consumer()
con.send(None)  #用来激活con
product(con)
