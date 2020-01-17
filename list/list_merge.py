def insertval(l, val):
    for index, v in enumerate(l):
        if (val <= v):
            l.insert(index, val)
            return
    l.append(val)


def insertlist(source, target):
    for v in source:
        if not target:
            target.append(v)
        else:
            insertval(target, v)
    return target


source1 = [3, 1, 8, 4, 4, 2, 9]
source2 = [2, 9, 0, 3, 6, 1]
target = []
insertlist(source1, target)
insertlist(source2, target)
print(target)
