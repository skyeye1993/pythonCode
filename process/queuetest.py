from multiprocessing import Process, Queue
import time


def task(q):
    print('start get num')
    msg = q.get()
    print('get msg:', msg)


if __name__ == '__main__':
    q = Queue(10)
    p = Process(target=task, args=(q,))
    p.start()
    time.sleep(1)
    print('p put msg')
    q.put(1)
    p.join()
