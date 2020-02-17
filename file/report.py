import random
import pygal

fmath = r'D:\math.txt'  # 路径前面加上r之后  只需要有一个\即可
fchinese = r'D:\chinese.txt'
fmerge = r'D:\merge.txt'
svgpath = r'D:\1.svg'


def createReport(fpath, num):
    f = open(fpath, 'w')
    for i in range(1, num + 1):
        info = '%d name_%d: %d\n' % (i, i, random.randint(30, 100))
        f.write(info)
    f.close()


def parseReport(fpath, obj, dreport):
    f = open(fpath, 'r')
    for line in f:
        index1, name, score = [val.strip(' :') for val in line.strip().split()]
        if index1 not in dreport:
            dreport[index1] = {}
        dreport[index1].setdefault('name', name)
        dreport[index1].setdefault(obj, score)


def mergeReport(fname, reportlist):
    f = open(fname, 'w')
    for i in range(1, 41):
        data = reportlist[str(i)]
        subkeys = list(data.keys())
        listinfo = '%d %s: ' % (i, data['name'])
        subkeys.remove('name')
        lscore = [data[subkey] for subkey in subkeys]
        listinfo += ' '.join(lscore)
        f.write(listinfo + '\n')
    f.close()


def searchById(id, reportlist):
    subd = reportlist[str(id)]
    subkeys = list(subd.keys())
    subkeys.remove('name')
    print([{key: subd[key]} for key in subkeys])
    result = [int(subd[key]) for key in subkeys]
    return result


def showScore(obj, reportlist):
    lscore = [reportlist[key][obj] for key in reportlist.keys()]
    sumscore = [sum(searchById(key, reportlist)) for key in reportlist.keys()]
    print(max(lscore))
    print(min(lscore))
    print(max(sumscore))
    print(min(sumscore))


def setval(dspread, score):
    key = '0-59'
    if score >= 60:
        if score == 100:
            ten = 90
        else:
            ten = score - score % 10
        key = ('%d-%d' % (ten, ten + 9 + (ten / 90)))
    dspread[key] += 1


def score_spread(obj, reportlist):
    keys = ['0-59']
    [keys.append('%d-%d' % (val, val + 9 + (val / 90))) for val in range(60, 100, 10)]
    dspread = dict.fromkeys(keys, 0)
    lscore = [int(reportlist[key][obj]) for key in reportlist.keys()]
    [setval(dspread, score) for score in lscore]
    return dspread


def gensvg(fpath, mathd, chinesed):
    keys = ['0-59']
    [keys.append('%d-%d' % (val, val + 9 + (val / 90))) for val in range(60, 100, 10)]
    line_chart = pygal.Bar()
    line_chart.title = 'Score Spread'
    line_chart.x_labels = keys
    line_chart.add('math', mathd.values())
    line_chart.add('chinese', chinesed.values())

    line_chart.render_to_file(fpath)


snum = 40
dreport = {}
createReport(fmath, snum)
createReport(fchinese, snum)
parseReport(fmath, 'math', dreport)
parseReport(fchinese, 'chinese', dreport)
print(dreport)
mergeReport(fmerge, dreport)
# searchById(1, dreport)
# showScore('math', dreport)
math = score_spread('math', dreport)
chinese = score_spread('chinese', dreport)
gensvg(svgpath, math, chinese)
