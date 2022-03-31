# 369 게임 
import random

for i in range(50):
    num = random.randrange(1, 101)
    num10 = int(num / 10)
    num1 = num % 10
    count = 0

    if num1 == 3 or num1 == 6 or num1 == 9:
        count += 1
    if num10 == 3 or num10 == 6 or num10 == 9:
        count += 1

    print()
    print(num, end = ' ')

    if count == 1:
        print("짝", end = ' ')
    elif count == 2:
        print("짝짝", end = ' ')


