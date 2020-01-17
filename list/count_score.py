def get_scorebyobj(listl, objid):
    """
    listFirst = []
    for lists in listl:
        listFirst.append(lists[objid])
    return listFirst
    """
    z = zip(*listl)
    for index, val in enumerate(z):
        if objid == index:
            return list(val)


def getaverage(listS):
    return int(sum(listS) / len(listS))


list_score = [[80, 90, 78], [88, 99, 100], [77, 88, 60]]
l = get_scorebyobj(list_score, 0)
print(l)
ave = getaverage(l)
print(ave)
