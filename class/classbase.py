class people(object):  #括号里中的object表示此类继承与object
    name = 'xuxianda'
    gender = '男'
    age = 12


p = people()
print(people.name, people.gender, people.age)
print(p.name, p.gender, p.age)
p.name = 'aaaaa'
print(people.name, people.gender, people.age)
print(p.name, p.gender, p.age)