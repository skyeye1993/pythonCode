list1 = [1, 2, 3, 4, 'abc', ['123']]
for val in list1:
    if isinstance(val, (str, list)):
        for tmp in val:
            print(tmp)
    else:
        print(val)
print('----------------------------------------------')
list2 = ['a', 'b', 'c']
r2 = range(len(list2))
for val in r2:
    print(val, list2[val])

index = 0
for val in list2:
    print(index, list2[index])
    index += 1

for index, val in enumerate(list2):
    print(index, val)
