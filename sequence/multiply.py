def multiply():
    for i in range(1, 10):
        result = ''
        for j in range(1, i + 1):
            f = '{y}*{x}={z}\t'
            result += f.format(x=i, y=j, z=i * j)
        print(result)

multiply()
