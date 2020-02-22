class newInt(int):
    def __new__(cls, num):
        print(num)
        obj = int.__new__(cls, abs(num))
        return obj


a = newInt(10)
b = newInt(-10)
print(a, b, type(a), id(a), id(b))


class single(object):
    obj = None

    def __new__(cls, num):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
        return cls.obj

    def __init__(self, num):
        print('call single init')
        self.arg = num


s1 = single(1)
s2 = single(2)
print(id(s1), id(s2), id(single(3)), id(single(4)))
print(s1.arg)
