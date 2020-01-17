import random


def generateScore(num):
    l = []
    for i in range(0, num):
        score = random.randint(40, 100)
        l.append(score)
    return l


def generateScore2(num, scoreName):
    s = {}
    for i in range(num):
        p = {}
        p[scoreName] = random.randint(40, 100)
        s[i + 1] = p
    return s


def mergelist(lmath, lchinese):
    l = zip(lmath, lchinese)
    num = 1
    result = {}
    for val in l:
        result[num] = list(val)
        num += 1
    return result


def mergelist2(lmath, lchinese):
    result = {}
    for index in range(len(lmath)):
        temp = {}
        temp['math'] = lmath[index]
        temp['chinese'] = lchinese[index]
        result[index + 1] = temp
    return result


def mergelist3(lmath, lchinese):
    for index in range(len(lmath)):
        lmath[index + 1].update(lchinese[index + 1])
    return lmath


def disctolist(disc):
    l = []
    for key in disc:
        l.append(disc[key])
    return l


def mycomp(disc):
    return sum(disc.values())


lmath = generateScore(40)
lchinese = generateScore(40)
# result = mergelist(lmath, lchinese)
# print(result)
# print(sum(result[3]))

# result = mergelist2(lmath, lchinese)
# print(result)
# print(result[3]['math'])
# print(sum(result[3].values()))

lmath = generateScore2(40, 'math')
lchinese = generateScore2(40, 'chinese')
result = mergelist3(lmath, lchinese)
print(result)

result2 = disctolist(result)
result2.sort(key=mycomp, reverse=True)
print(result2)
