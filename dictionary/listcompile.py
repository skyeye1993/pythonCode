keys = [chr(val) for val in range(ord('a'), ord('z') + 1)]
print(keys)

import random

nums = [random.randint(1, 100) for i in range(10)]
print(nums)

num = 234
strs = [int(c) for c in str(num)]
print(strs)
