#raise 主动触发异常

def fun(a, b):
    assert b != 0, 'b is zero'
    if b == 0:
        raise ValueError('b is zero')
    return a / b


def foo(vals):
    assert isinstance(vals, list), 'vals is not list'
    if not isinstance(vals, list):
        raise TypeError('vals is not list')
    vals = [int(val) for val in vals]
    return sum(vals)


print(fun(10, 2))
# print(fun(10, 0))
print(foo(list('12345')))
print(foo(123))
