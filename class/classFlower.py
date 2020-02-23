class Flower(object):
    name = ''
    color = ''

    def grow(self):
        print('Flower grow')

    def __init__(self, name, color):
        print('Flower init')
        self.name = name
        self.color = color


class Rose(Flower):
    price = 0

    def __init__(self, name, color, price):
        print('Rose init')
        self.price = price
        super(Rose, self).__init__(name, color)

    def grow(self):
        print('Rose grow')

    def show(self):
        print(self.name, self.color, self.price)

    def __str__(self):
        print('call __str__')
        return self.color + ' ' + str(self.price)

    def __repr__(self):
        return 'Rose Class Object'

    def __add__(self, other):
        return self.price + other.price

    def __mul__(self, other):
        return self.price * other


rose = Rose('rose', 'red', 5)
rose.show()

listl = list('123')
print(listl, repr(listl))
r = rose + rose
print(r, r * 5)
