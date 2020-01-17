f1 = '%s is %s'
print(f1 % ('apple', 'fruit'))

f2 = '{} is {}'
print(f2.format('apple', 'fruit'))

f3 = '{0} is {1}'
print(f3.format('apple', 'fruit'))

f4 = '{1} is {0}'
print(f4.format('fruit', 'apple'))

f5 = '{key} is {value}'
print(f5.format(key='apple', value='fruit'))
