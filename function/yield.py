listnum = []
for i in range(0, 100):
    if i % 2 == 0:
        listnum.append(i)
print(listnum)
print([val for val in range(0, 100) if val % 2 == 0])
print(list(filter(lambda val: val % 2 == 0, range(0, 100))))


#生成器

def gen_even():
    for val in range(0, 100):
        print('val=', val)
        if val % 2 == 0:
            print('yield', 1)
            yield val
            print('yield', 2)


gen = gen_even()
next(gen)
next(gen)
next(gen)


def gen_data():
    val = yield 1
    print(val)
    val = yield 2
    print(val)

gen = gen_data()
print(next(gen))
print(gen.send('abc'))   # send 发送并返回一个值
gen.close()