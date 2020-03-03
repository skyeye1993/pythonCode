import os

path = '11.txt'


class FileError(IOError):
    print('fileError')


result = os.path.exists(path)
if not result:
    raise FileError('File not found','')
