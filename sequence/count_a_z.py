def count_max(str):
    max_count = 0
    max_char = ''
    for i in range(97, 123):
        count = str.count(chr(i))
        if count > max_count:
            max_count = count
            max_char = chr(i)
    return max_char, max_count


str1 = 'aaabbbbcccccddddddd'
print(count_max(str1))
