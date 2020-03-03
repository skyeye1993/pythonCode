def func(d, key):
    try:
        k = int(key)
        print(d[k])
    except (KeyError, ValueError) as e:
        print('catch exception : ', e)

d = {10:100}
func(d,'dd')