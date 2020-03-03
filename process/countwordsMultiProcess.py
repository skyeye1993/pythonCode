import os
import time
import multiprocessing

path = 'D:\英文小说原著大全'


def countfile(fpath):
    flist = []
    gen = os.walk(fpath)
    for tpath, dirs, files in gen:
        for name in files:
            fname = os.path.join(tpath, name)
            flist.append(fname)
    return flist


def countwords(flist):
    wds = 0
    for fname in flist:
        wds += countwordsbyfile(fname)
    print(wds)
    return wds


def countwordsbyfile(fname):
    result = 0
    with open(fname, errors='ignore') as f:
        for line in f:
            wds = line.strip().split()
            result += len(wds)
    return result


if __name__ == "__main__":
    s_time = time.time()
    flist = countfile(path)
    midnum = int(len(flist)/2)
    multiprocessing.freeze_support()
    p = multiprocessing.Process(target=countwords, args=(flist[midnum:],))
    p.start()
    countwords(flist[:midnum])
    p.join()
    print(s_time, time.time())
