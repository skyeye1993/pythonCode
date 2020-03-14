from threading import Thread


def thread_func():
    print('call thread_func')
    while (True):
        pass


def create_thread():
    t = Thread(target=thread_func)
    t.start()
    return t


if __name__ == '__main__':
    t = create_thread()
    t.join()
