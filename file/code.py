s = u'中国'  # 表示编码是unicode
print(ord(s[0]))  # 打印 ‘中’ 的unicode地址
print(hex(ord(s[0])))  # 0x4e2d
print(u'\u4e2d')
