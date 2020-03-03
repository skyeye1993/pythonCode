import os
import time
import multiprocessing
from multiprocessing import Queue

path = 'D:\英文小说原著大全'


def countfile(fpath):
    flist = []
    gen = os.walk(fpath)
    for tpath, dirs, files in gen:
        for name in files:
            fname = os.path.join(tpath, name)
            flist.append(fname)
    return flist


class ParseFileList(multiprocessing.Process):
    flist = []

    def __init__(self, flist, que):
        self.flist = flist
        self.q = que
        super(ParseFileList, self).__init__()

    def countwordsbyfile(self, fname):
        result = 0
        with open(fname, errors='ignore') as f:
            for line in f:
                wds = line.strip().split()
                result += len(wds)
        return result

    def countwdsbyflist(self):
        wds = 0
        for fname in self.flist:
            wds += self.countwordsbyfile(fname)
        self.q.put(wds)
        print(wds)

    def run(self):
        self.countwdsbyflist()


if __name__ == "__main__":
    q = Queue(10)
    s_time = time.time()
    flist = countfile(path)
    snum = int(len(flist) / 2)
    p = ParseFileList(flist[snum:], q)
    p.start()
    mainP = ParseFileList(flist[:snum], q)
    mainP.run()
    p.join()
    print(q.get_nowait()+q.get_nowait())
    print(s_time, time.time())
