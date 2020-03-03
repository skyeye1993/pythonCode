# 创建进程池
from multiprocessing import Pool
import multiprocessing
import os
import time


def task(num):
    print('run task', num, os.getpid())
    time.sleep(2)
    return str(num)


if __name__ == "__main__":
    pool = Pool(processes=3)
    result = []
    print(multiprocessing.active_children())
    for i in range(10):
        result.append(pool.apply_async(task, (i,)))
    pool.close()
    pool.join()
    for i in range(10):
        print(result[i].get())
