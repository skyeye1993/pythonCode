import random


def getrcode(N):
    listN = '1234567890'
    listC = ''
    rcode = ''
    for i in range(97, 123):
        listC += chr(i)
    print(listC)

    numN = random.randint(1, N - 1);
    numC = N - numN
    for i in range(numC):
        rcode += random.choice(listC)
    for i in range(numN):
        rcode += random.choice(listN)
    return rcode


print(getrcode(5))
