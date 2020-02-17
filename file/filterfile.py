def filterFile(sourcepath):
    sourcefile = open(sourcepath, 'r')
    flag = False
    script = ''
    for l in sourcefile:
        if flag:
            if l.strip().endswith(script):
                flag = False
        elif l.strip().startswith('"""'):
            flag = True
            script = '"""'
        elif l.strip().startswith("'''"):
            flag = True
            script = "'''"
        elif l.strip() == '':
            continue
        elif l.strip().startswith('#'):
            continue
        elif '#' in l:
            print(l[:l.find('#')].strip())
        else:
            print(l.strip())


filterFile('test.py')
