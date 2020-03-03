import os
import time

path = 'D:\英文小说原著大全'


def countwordsbyfile(fname):
    result = 0
    with open(fname,errors='ignore') as f:
        for line in f:
            wds = line.strip().split()
            result += len(wds)
    print(fname, result)
    return result


def countwords(fpath):
    result = 0
    gen = os.walk(fpath)
    # print(list(gen))
    for tpath, dirs, files in gen:
        print(tpath, dirs, files)
        for name in files:
            fname = os.path.join(tpath, name)
            result += countwordsbyfile(fname)
    print(result)
    return result


if __name__ == "__main__":
    s_time = time.time()
    countwords(path)
    print(s_time, time.time())
