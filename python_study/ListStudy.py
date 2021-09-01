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

print("리스트 검색")
listLetter = "This is a book that is a pencil".split()
# for letter in listLetter:
#     print(letter)

i = listLetter.index('that') # 4
n = listLetter.count('a') # 2

# print("i:" + i + "n:" + n)
print(i+n)

print("List Comprehension")
# [표현식 for 요소 in 컬렉션 [if 조건식] ]

#n의 제곱을 구하는데, n은 0~9 까지 숫자들 중이고, 그 숫자들중에서 3의 배수인 게 n임
ComprehensionTest = [n ** 2 for n in range(10) if n % 3 == 0]
print(ComprehensionTest)



