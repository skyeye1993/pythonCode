import random

value = random.randint(0, 100)
while True:
    tmp = int(input("Enter a number [0,100]:"))
    print(tmp)
    if value > tmp:
        print('small')
    elif tmp > value:
        print('big')
    else:
        print('guessOk')
        break
print('Over')
