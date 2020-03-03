from multiprocessing import Value, Process, Lock

val = Value('i', 10)
lock = Lock()

def task(val, lock):
    num = 100000
    while num > 0:
        lock.acquire()
        if val.value > 0:
            print('-1 in task val:', val.value)
            val.value -= 1
            print('-2 in task val:', val.value)

        lock.release()
        num -= 1


def product(val, lock):
    num = 1000000
    while num > 0:
        lock.acquire()
        if val.value < 0:
            print(' in product val:', val.value)
        val.value += 1
        print ('+2 in product val:', val.value)
        lock.release()
        num -= 1


if __name__ == '__main__':
    p = Process(target=product, args=(val, lock))
    p.start()
    p1 = Process(target=task, args=(val, lock))
    p1.start()
    task(val, lock)
    p.join()
    p1.join()
