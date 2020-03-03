def test(fname):
    try:
        mnames = []
        f = open(fname)
        for line in f:
            result = line.split()
            print(float(result[1]))
            mnames.append(result[0])
        return mnames
    except:
        print('catch an exception')
        return mnames
    finally:
        f.close()
        print('do finally')
        return 111


fpath = 'D:\\important\\pythonCode\\exception\\moviePlay.txt'
print(test(fpath))
