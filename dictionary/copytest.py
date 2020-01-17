import copy

minfo = ['Mermaid', 'zxc', ['love', 'chinese'], ['dc', 'lzx']]
m1 = minfo
m2 = list(minfo)
m3 = minfo[:]
m4 = copy.copy(minfo)
print(id(minfo), id(m1), id(m2), id(m3), id(m4))  # m1 m2 m3 m4都是浅拷贝
m1[0] = 'mid'  # 只有m1修改了(字符串是不可变序列)
print(m1, m2, m3, m4)
m2[2].append('english')
print(m1, m2, m3, m4)  # m1,m2,m3和m4的数组都修改了
print(id(m1[2]), id(m2[2]), id(m3[2]), id(m4[2]))  # 全部都是浅拷贝

m5 = copy.deepcopy(minfo)
print(minfo, m5)
minfo[3].append('aaa')
print(minfo, m5)
print(id(minfo[3]), id(m5[3]))
