class people(object):
    name = 'X'
    gender = 'X'
    __age = 111  #属性前面加上两个_，表示私有属性

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getGender(self):
        return self.gender

    def setGender(self, gender):
        self.gender = gender

    def getAge(self):
        print(id(self.__age))
        return self.__age

    def setAge(self, age):
        self.__age = age

    @property
    def Age(self):
        print('call Age()')
        return self.__age
    @Age.setter
    def Age(self,age):
        self.__age = age

p = people()
print(p.getAge())
p.Age=222
print(p.Age)