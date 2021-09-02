# coding=utf-8
a = 1
b = 2
c = a+b
print(c)

x = 1

if x > 0:
    a = 1
    b = 2
    c = a + b
else :
    a = 2
    b = 5
    c = a + b

print (c)

import math

n = math.sqrt(9.0)

print(n)

#주석 처리

a = None
print(a is None)
print(a is not None)
print("-------------------")

print(bool(0)) # false
print(bool("dfdfd")) #true
print(bool("False")) #true
print(bool()) #false

print("----------연산자 공부-----------")

print("멤버쉽 연산자")

a=[1,2,3,4,5]
b = 3 in a
c = 7 in a
print(b) # True
print(c) # False
print(b + c)

import main

main.print_hi("김민재")

def print_test (test_letter):
    print(test_letter)

print_test("test")

print("문자열 포맷팅 연습")
s = "이름 : %s 나이 : %d" % (["김민재", "김민서"], 30)
print(s)

print("문자열 클래스")

x = "ABC"
print(type(x))
print(x[0])
a = x[0]
print(type(a))

departure, _, arrival = "seattle-seoul".partition("-")
print(departure)
print(arrival)

items = "ab,cd,ef".split(",")
print(items)

for item in items: #iter
    print(item)

print("조건문 (if)")

x = 10
if x < 10 :
    print("한자리수")
elif x < 100 :
    print("두자리수")
else :
    print ("세자리 이상 ")

sum = 0
for i in range(11): # 0~ n-1 까지 반복
    sum += i
print(sum)

print("range(1, 2, 3) : 파라미터가 3개까지 올 수 잇음 (start, stop, step ")

numbers = range (2, 15, 3)
for n in numbers:
    print(n)


# __init__.py 에 초기화를 해주는 것. __all__이라는 리스트 변수에 넣어줘야한다.
from models.account import *
bill.charge(1, 50)








