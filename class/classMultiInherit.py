class A(object):
    def test(self):
        print('A:test')

    def testA(self):
        print('testA')


class B(object):
    def test(self):
        print('B:test')

    def testB(self):
        print('testB')

class C(A,B):
    pass

c = C()
c.testA()
c.testB()
c.test()
print(C.mro())