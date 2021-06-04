# coding=utf-8
'''
try-except用例:
需求:猜数字游戏
1: 开始游戏产生一个1~100随机数
2: 用户输入，游戏根据输入值提示大或者小
3: 用户根据提示继续输入，知道猜中为止
4: 如果用户输入错误，程序可以处理异常。
'''
import random

num = random.randint(0, 100)

while True:
    try:
        guess = int(input("Enter 1~100:"))
    except ValueError as e:
        print("Input value is invalid!!")
        continue
    if guess > num:
        print("guess Bigger:", guess)
    elif guess < num:
        print("guess Samller:", guess)
    else:
        print("Guess OK, Game Over")
        break
    print("\n")