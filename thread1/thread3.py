from threading import Thread
import time

num = 0


def producer():
    global num
    count = 100
    while count > 0:
        num += 1
        print('producer:', num)
        count -= 1
        time.sleep(0.1)


def consumer():
    global num
    count = 100
    while count > 0:
        if num > 0:
            num -= 1
            print('consumer:',num)
            count -= 1
            time.sleep(0.1)


def createThread(func):
    t = Thread(target=func)
    t.start()
    return t


if __name__ == '__main__':
    t = createThread(consumer)
    producer()
    t.join()