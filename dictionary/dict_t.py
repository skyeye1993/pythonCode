import random

s = {}

for i in range(1, 41):
    s[i] = random.randint(30, 100)
print(s)

def getScore(discS, score):
    d = []
    for key in discS.keys():
        if (discS[key] >= score):
            d.append(key)
    return d


print(getScore(s, 60))
