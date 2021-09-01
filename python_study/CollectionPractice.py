# coding=utf-8
#List

"""
List 는 동적 배열 (Dynamic Array)로서 자유롭게 확장할 수 있다.

List의 요소들은 [ ] 으로 둘러 쌓여 컬렉션을 표현한다.
각 요소들은 서로 다른 타입이 될수 있으며 , 로 구분한다.

"""

a = ["AB", 20, True]
for element in a:
    print(element)

letter = a[0]
print(letter)
a[0] = "ABC" # List element 수정
letter = a[0]
print(letter)
for element in a:
    print(element) # 수정된 element 출력

testList = [1,3,5,7,9,11,13,15,17]
a = testList[0:4] #1, 3, 5, 7
print(a)
b = testList[:3] #1, 3, 5
print(b)
c = testList[5:] # 11, 13, 15, 17
print(c)

print("List 추가, 수정, 삭제")
testList1 = ["AB", 123, True]
#추가
testList1.append("Plus")
#수정
testList1[1] = 456
#삭제
del testList1[2]

for element in testList1:
    print(element)

print("list 병합 및 반복")

listA = [1, 2, 3]
listB = [4, 5, 6]
result = listA + listB
print(result)

resultMul = listA * 3
print(resultMul)

print







