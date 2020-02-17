import random

filepath = 'D:\\report.txt'
passpath = 'D:\\pass.txt'


def createFile(filepath, num):
    f = open(filepath, 'w')
    for i in range(1, num + 1):
        info = '%d name_%d: %d\n' % (i, i, random.randint(30, 100))
        f.write(info)
    f.close()


def createPassFile(sourcepath, targetpath):
    source = open(sourcepath,'r')
    target = open(targetpath,'w')
    for line in source:
        l = line.strip().split(' ')
        score = int(l[-1])
        if score >= 60:
            target.write(line)
    source.close()
    target.close()

createFile(filepath, 40)
createPassFile(filepath, passpath)
