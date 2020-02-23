import time
class sharebike(object):
    name = ''
    price = 0
    s_time = 0
    e_time = 0
    __isFree = False

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def isFree(self):
        return self.__isFree

    @isFree.setter
    def isFree(self, flag):
        self.__isFree = flag

    def lock(self):
        self.s_time = time.time()

    def unlock(self):
        self.e_time = time.time()

    def pay(self):
        if self.__isFree:
            return 0
        tlens = self.e_time - self.s_time
        money = (1+int(tlens/3600))*self.price
        return money
    def get_times(self):
        return str(int((self.e_time - self.s_time)/60)) + ':'\
               + str(int((self.e_time - self.s_time)%60))

ofo = sharebike('ofo',1)
ofo.unlock()
time.sleep(2)
ofo.lock()
ofo.isFree = True
print(ofo.pay())