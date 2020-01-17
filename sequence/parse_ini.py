settings = '[letv] name=letest pwd=abc123 [iqiyi] name=iqiyitest pwd=abc123'


def get_session():
    s_index = 0
    e_index = 0
    while True:
        print('find index=', s_index)
        s_index = settings.find('[', e_index)  # 从e_index位置开始查找
        if s_index != -1:
            e_index = settings.find(']', s_index)
            print(s_index, e_index, settings[s_index + 1:e_index])
        else:
            break


get_session()
