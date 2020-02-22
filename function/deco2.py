import time


def LogInit(tag):
    def Log(func):
        print('call log')
        def LogOut(msg):
            times = time.strftime('%Y-%m-%d:%H-%M-%S')
            msg = tag + ',' + times + ',' + msg
            func(msg)
        return LogOut
    return Log


@LogInit('Debug')
def Logd(msg):
    print('%s' % msg)


Logd('test')
