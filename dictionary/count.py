def getStrCount(msg):
    count = {}
    for c in msg:
        if c not in count:
            count.setdefault(c, 1)
        else:
            num = count.get(c)
            count.update({c: num + 1})
    return count


def getStrCount2(msg):
    atoz = ''
    for c in range(ord('a'), ord('z') + 1):
        atoz += chr(c)
    d = dict.fromkeys(atoz, 0)

    for c in msg:
        if c.strip() == '':
            continue
        num = d[c]
        d[c] = num + 1
    keys = list(d.keys())
    for k in keys:
        if d[k] == 0:
            d.pop(k)
    return d


msg = 'this is python'
print(getStrCount(msg))
print(getStrCount2(msg))
