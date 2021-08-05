"""
동전 교환 프로그램
==================
교환할 돈은 얼마입니까? 2763 (엔터키)

결과:
오백원짜리 ===> 5개
백원짜리 ===> 2개
오십원짜리 ===> 1개
십원짜리 ===> 1개
나머지 바꾸지 못한 잔돈 ===> 3원
"""

money, c500, c100, c50, c10 = 0, 0, 0, 0, 0
money = int(input("교환할 돈 입력 : "))

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print()
print("오백원짜리 ===> %d개" % c500)
print("백원짜리 ===> %d개" % c100)
print("오십원짜리 ===> %d개" % c50)
print("십원짜리 ===> %d개" % c10)
print("바꾸지 못한 잔돈 ===> %d원" % money)

#################################################################################

"""
윤년 계산 프로그램
-------------------
1) 기원 연수가 4로 나누어 떨어지는 해는 우선 윤년으로 한다.
2) 그 중에서 100으로 나누어 떨어지는 해는 평년으로 한다.
3) 다만 400으로 나누어 떨어지는 해는 다시 윤년으로 정한다.

연도를 입력 : 2019(엔터)
결과 : 윤년입니다.(윤년이 아닙니다)
"""

year = 0
year = int(input("연도 입력 : "))

if(((year%4 == 0) and (year%100 != 0)) or (year%400 == 0)):
    print("%d년은 윤년입니다." % year)
else:
    print("%d년은 윤년이 아닙니다." % year)
    
#################################################################################

"""
전자 계산기 프로그램(사칙연산)
----------------------------------
연산자 : +
숫자1 : 10
숫자2 : 5

결과 : 10 + 5 = 15
"""

print("***************************************")
print("          전자 계산기 프로그램         ")
print("***************************************")
print()
op = input("연산자 : ")
num1 = int(input("숫자1 : "))
num2 = int(input("숫자2 : "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
else:
    result = num1 / num2
    
print("\n결과 : {} {} {} = {}".format(num1, op, num2, result))

#################################################################################

"""
(가위, 바위, 보) 중에서 하나를 선택 : 가위(엔터)

컴퓨터 : 보, 사용자 : 가위
사용자가 이겼습니다.
"""

import random

player = input("(가위, 바위, 보) 중에서 하나를 선택 :")
number = random.randint(0, 2)

if number == 0:
    computer = "가위"
elif number == 1:
    computer = "바위"
else:
    computer = "보"
    
print("사용자 : {}, 컴퓨터 : {}".format(player, computer))

if player == computer:
    print("비겼음")
elif player == "바위":
    if computer == "보":
        print("컴퓨터가 이겼음")
    else:
        print("사용자가 이겼음")
elif player == "보":
    if computer == "바위":
        print("사용자가 이겼음")
    else:
        print("컴퓨터가 이겼음")
elif player == "가위":
    if computer == "바위":
        print("컴퓨터가 이겼음")
    else:
        print("사용자가 이겼음")
        
#################################################################################

"""
전자 계산기 프로그램을 반복문을 이용하여 업그레이드
(끝나는 조건은 연산자에 x 를 입력하면 종료)
"""

print("***************************************")
print("          전자 계산기 프로그램         ")
print("***************************************")
print()

while True:
    op = input("연산자 : ")
    
    if op == 'x': break
        
    num1 = int(input("숫자1 : "))
    num2 = int(input("숫자2 : "))
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    else:
        result = num1 / num2

    print("\n결과 : {} {} {} = {}".format(num1, op, num2, result))
    
#################################################################################

"""
가위 바위 보게임을 반복문을 이용하여 업그레이드
(끝나는 조건은 x나 q를 입력하면 종료)

끝날 때 결과에 ?승 ?패 출력
"""

import random

win, fail = 0, 0
while True:
    player = input("(가위, 바위, 보) 중에서 하나를 선택 :")
    
    if player in ["x", "q"]: break
        
    number = random.randint(0, 2)

    if number == 0:
        computer = "가위"
    elif number == 1:
        computer = "바위"
    else:
        computer = "보"

    print("사용자 : {}, 컴퓨터 : {}".format(player, computer))

    if player == computer:
        print("비겼음")
    elif player == "바위":
        if computer == "보":
            print("컴퓨터가 이겼음")
            fail += 1
        else:
            print("사용자가 이겼음")
            win += 1
    elif player == "보":
        if computer == "바위":
            print("사용자가 이겼음")
            win += 1
        else:
            print("컴퓨터가 이겼음")
            fail += 1
    elif player == "가위":
        if computer == "바위":
            print("컴퓨터가 이겼음")
            fail += 1
        else:
            print("사용자가 이겼음")
            win += 1
            
print("{}승 {}패".format(win, fail))

#################################################################################

"""
숫자를 입력받아 짝수의 합과 홀수의 합을 구하시오.(0을 입력하면 종료)

2
3
1
6
0
---
짝수의 합: ?
홀수의 합: ?
"""
even, odd = 0, 0
while True:
    num = int(input(""))
    
    if num == 0:
        break
    elif num % 2 == 0:
        even += num
    else:
        odd += num
        
print("짝수의 합 : ", even, " \t 홀수의 합 : ", odd)

#####################################################################

"""
숫자 맞추기 게임
=================
1부터 100사이의 숫자를 맞추시오

숫자입력 : 50
낮음!

숫자입력 : 75
낮음!

...

숫자입력 : 89
정답입니다! ~~ 시도회수 : 7번
"""

import random

cnt = 0
number = random.randint(1, 100)

print("1부터 100사이의 숫자를 맞추시오")

while cnt < 10:
    guess = int(input("숫자 입력 : "))
    cnt += 1
    
    if guess < number:
        print("낮음!")
    elif guess > number:
        print("높음!")
    else:
        break
    
if guess == number:
    print("축하합니다. 시도횟수 = ", cnt)
else:
    print("정답은 : ", number)
    
############################################################################

"""
숫자 맞추기 게임
=================
1부터 100사이의 숫자를 맞추시오

숫자입력 : 50
낮음!

숫자입력 : 75
낮음!

...

숫자입력 : 89
정답입니다! ~~ 시도회수 : 7번
"""

import random

cnt = 0
number = random.randint(1, 100)

print("1부터 100사이의 숫자를 맞추시오")

while cnt < 10:
    guess = int(input("숫자 입력 : "))
    cnt += 1
    
    if guess < number:
        print("낮음!")
    elif guess > number:
        print("높음!")
    else:
        break
    
if guess == number:
    print("축하합니다. 시도횟수 = ", cnt)
else:
    print("정답은 : ", number)
