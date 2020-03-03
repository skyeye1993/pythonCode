import os
import multiprocessing
import time


def task():
    print(os.getpid(), os.getppid())
    print('call in task')
    time.sleep(1)
    i = 0
    while i < 100:
        time.sleep(.1)
        print('call task:', i)
        i += 1
    print('task exit')


if __name__ == '__main__':
    multiprocessing.freeze_support()
    p = multiprocessing.Process(target=task)
    print('main pid:', os.getpid())
    p.start()
    i = 0
    print(p.ident)  # 当前进程号
    # p.terminate()  # 结束p进程
    while i < 100:
        time.sleep(.1)
        print('call main:', i)
        i += 1
    # p.join()  # 等待线程执行完成
    print('main exit')
