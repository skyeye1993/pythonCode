l1 = [1, 2, 3, 4]
print(l1)

l2 = [1, 2, 3, [1, 2, 3]]
print(l2)

for i in l2:
    print(i)

l3 = ['a', 'b', 'c']
print('_'.join(l3))

print(sum(l1))
print(len(l1))
print(zip(l1))
print(list(zip(l1)))
print(list(zip(l1,'abcd')))