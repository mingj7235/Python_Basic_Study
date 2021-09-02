"""
Function
    - 일정한 작업을 수행하는 코드 블럭
    - def 키워드를 사용하여 정의함

    def 함수명 (parameter) :
        logic ...
        return 리턴값
"""


def sum(a, b):
    s = a + b
    return s


total = sum(5, 8)
print(total)

print("-------------")


def f(i, mylist):
    i += 1
    mylist.append(0)


k = 10  # k 는 int -> immutable 즉, 변경불가능 정수는 immutable 타입이다.
m = [1, 2, 3]  # m 은 List -> mutable List는 mutable 타입이다.

f(k, m)
f(k, m)
print(k, m)

"""
Default parameter
    - function에 전달되는 파라미터중 호출자가 전달하지 않으면 디폴트로 지정된 값을 사용하게 할 수 있다.
    - Optional 파라미터라고 부르기도한다. 
"""


def cal(i, j, f=1):
    return (i + j) * f


print(cal(2, 4))

"""
named parameter
    - parameter에 이름을 부여하여 쉽게 파악할 수 있도록함
"""


def report(name, age, score):
    print(name, age, score)


report(age=10, name="ABC", score="A")

"""
가변 길이 파라미터
    - 입력 파라미터의 갯수를 미리 알 수 없거나, 0부터 N개의 파라미터를 받아들이도록 하고싶을 때 사용. 
    - 파라미텨 명 앞에 *를 붙여 가변길이임을 표시한다. 
"""


def total(*numbers):
    tot = 0  # 초기화
    for number in numbers:
        tot += number
    return tot

t = total (1,2,3,4)
print(t)
nt = total(2,4,6,7,8)
print(nt)

"""
Return 값
    - Python 에서는 return 값이 하나 이상일 수 있다. 필요한 수만큼 return 키워드 다음에 콤마로 구분하여 적는다. 
    - 사실, 여러개의 return값이 아니라, Tuple로 묶어서 하나를 리턴하는 것이므로, 하나의 리턴값을 전달한다고 볼 수 있다. 
    
"""

print("multi return (tuple return) test")
def calc (*numbers) :
    count = 0
    tot = 0
    for number in numbers:
        count += 1
        tot += number
    return count, tot

print(calc(1,2,3,4,5))
print(type(calc(1,2,3,4,5)))

count, tot = calc(1,2,3,4,5)

print ("count : %d , tot : %d" % (count, tot))
print(f"count : {count}, tot : {tot}")
