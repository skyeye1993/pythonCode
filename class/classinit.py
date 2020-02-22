class people(object):
    name = 'X'
    __age = 'X'
    gender = 'X'

    def __new__(cls, *args, **kwargs):   #新建对象
        print('call new')
        obj = object.__new__(cls)
        return obj

    def __init__(self, name, age, gender): #初始化对象属性
        print(name, age, gender)
        self.name = name
        self.__age == age
        self.gender = gender
        print('call __init__')

    def __del__(self):   #垃圾回收
        print('call del')

    def getName(self):
        return self.name

    def setName(self, Name):
        self.name = Name

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, age):
        self.__age = age

    def getGender(self):
        return self.gender

    def setGender(self, Gender):
        self.gender = Gender

    def eat(self, food):
        print('eat', food)

    def sleep(self, times):
        pass


p1 = people('zhangsan', 100, 'female')
print(type(p1))
print(p1.name, p1.Age, p1.gender)
