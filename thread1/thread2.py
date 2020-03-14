from threading import Thread
import threading

def thread_func():
    print('call thread_func')
    print(threading.active_count())
    for i in threading.enumerate():
        print(i)


def create_thread():
    t = Thread(target=thread_func)
    t.start()
    return t


if __name__ == '__main__':
    t = create_thread()
    t.setName('t1')
    t.join()
