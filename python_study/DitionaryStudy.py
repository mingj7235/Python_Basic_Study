"""
Dictionary는 key-value 쌍을 요소로 갖는 컬렉션 (Map)
    - Hash Table 구조를 갖는다.
    - Python 에서 Dictionary는 Dict클래스로 구현되어 있다.
    - Dictionary의 key는 그값을 변경할 수 없는 immutable 타입이어야 한다. (value는 변경가능)
        즉, Dicionary의 key는 문자열이나 Tuple은 사용될 수 있으나, List는 키로 사용될 수 없다.
    - { } 를 사용하여 컬렉션을 표현한다. 'Key:Value' 쌍으로 되어있으며, 요소간은 콤마로 구분한다.
    - 특정 요소를 찾아 읽고 쓰기 위해서는 Dict변수명[키] 와같이 key를 인덱스와 같이 사용한다.
"""

scores = {"철수": 90, "민수": 80, "영희": 70}
v = scores["철수"]
print(v)

scores["민수"] = 88  # value 변경
print(scores["민수"])

"""
dict() 생성자로 dictionary를 생성할 수 있다. 
    - Tuple 리스트를 받아들이거나
    - 키-값을 직접 파라미터로 지정하는 방식도 가능하다.
"""

persons = [("김기수", 30), ("홍대길", 40), ("강찬수", 50)]
print(type(persons))  # List
print(type(persons[0]))  # tuple

mydict = dict(persons)
print(type(mydict))  # dict
print(mydict)
print(mydict["강찬수"])

scores = dict(a=80, b=70, c=60)
print(type(scores))
print(scores['a'])

scores['d'] = 70  # dict에 이렇게 그냥 추가하면된다.
print(scores)

del scores['b']
print(scores)

print("=============")
for score in scores:
    val = scores[score]
    print("%s : %d" % (score, val))

"""
dict 메서드

"""

scores = {"a": 20, "b": 30, "c": 40}
# key
keys = scores.keys()
for key in keys:
    print(key)

# value
values = scores.values()
for value in values:
    print(value)

# items
items = scores.items()
for item in items:
    print(item)

itemList = list(items)
print(type(itemList))
print(itemList[0])




