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





