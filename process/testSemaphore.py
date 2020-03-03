#coding:utf-8
from multiprocessing import Semaphore, Lock, Process
from array import array
import time, random

se = Semaphore(5)
ar = array('i', range(5))
lock = Lock()

def eat(se, ar, lock, idnum):
    se.acquire()
    lock.acquire()

    for index, val in enumerate(ar):
        if val == 0:
            ar[index] = 1
            break
    lock.release()
    print(idnum, 'ar_index', index)
    time.sleep(random.uniform(0, 1))
    lock.acquire()
    ar[index] = 0
    print(idnum, 'leave', index)
    lock.release()
    se.release()
if __name__ == '__main__':
    for i in range(20):
        p = Process(target=eat, args=(se, ar, lock, i))
        p.start()








