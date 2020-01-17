settings = '[letv] name=letest pwd=abc123 [iqiyi] name=iqiyitest pwd=abc123'

def get_sinfo(str):
    str = str.strip(' ')
    s_index = str.find('[')
    e_index = str.find(']')
    print(str[s_index+1:e_index])
    kvs = str[e_index+1:].split()
    for kv in kvs:
        print(kv.split('='))



def get_allsession(str):
    s_index = 0
    e_index = 0
    while True:
        s_index = str.find('[', e_index)
        e_index = str.find('[', s_index + 1)
        if e_index == -1:
            print(str[s_index:])
            get_sinfo(str[s_index:])
            break
        else:
            print(str[s_index:e_index])
            get_sinfo(str[s_index:e_index])


get_allsession(settings)
