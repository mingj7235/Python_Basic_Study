"""
Set 은 중복이 없는 요소들로만 구성된 집합 컬렉
    - {} 을 사용하여 컬렉션을 표현함. (dict와같음)
    - 순서대로 저장하지 않는다.
    - 리스트나 튜플등을 set으로 변경하기 위해서는 set()생성자를 사용한다.  -> 리스트에 중복된 값이 있을 때 중복없이 unique한 값만을 얻고자 할 때 유용

"""

# set 정의

setTest = {1, 2, 2, 2, 3, 4, }
print(setTest)

# set() 메소드

listTest = [1, 1, 1, 2, 2, 3]
print(listTest)
changeListToset = set(listTest)
print(changeListToset)

# set 추가 및 삭제

"""
- 새로운 요소를 추가하기 위해서는 set 클래스의 add() 메소드 사용
- 한번에 추가하기 위해서는 update() 메소드 사용 

- 요소 하나 삭제하기위해서는 remove() or discard() 메소드 사용
- 한번에 지우기위해서는 clear() 사용
"""

setTest = {1, 2, 3, 4, 5}

# 하나추가
setTest.add(6)
print(setTest)

# 여러개 추가
setTest.update({7, 8, 9})
print(setTest)

setTest.remove(2)
print(setTest)

setTest.clear()
print(setTest)

"""
- set 집합 연산

교집합 : &
합집합 : |
차집합 : -
"""

a = {1, 3, 5}
b = {1, 5, 9}

i = a & b  # 교집합
print(i)

j = a | b  # 합집합
print(j)

t = a - b # 차집합
print(t)



