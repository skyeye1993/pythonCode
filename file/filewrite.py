listl = ['java', 'python', 'c', 'c++']
path = 'D:\\abc.txt'
f = open(path, 'w')
# f.writelines(listl)
f.writelines([val + '\n' for val in listl])

import os

print([ord(val) for val in os.linesep])
print(ord('\r'), ord('\n'))

help(open)