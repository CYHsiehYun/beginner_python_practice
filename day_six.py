'''
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
'''

import random

answer = random.randint(1,100)

while True:
    number = int(input("enter your answer"))
    if number != answer :
        if answer > number :
            print("wrong answer be heigher!")
        elif answer < number:
            print("wrong answer be lower!")
    else:
        print("right answer!")
