'''
클래스
    - 속성 (attribute) + 메서드(method) = 클래스
    - 논리적 컨테이너
    - Python은 다른 OOP와 달리, Dynamic Language로서, 새로운 attribute를 실행중 동적으로 추가할 수 있다...  어마무시한 python... 'ㅁ'...
'''


class Rectangle:
    count = 0  # 클래스 변수

    # 초기자
    """
    초기자 (Initializer)
        - 클래스로부터 새 객체를 생성할 때 마다 실행되는 특별한 메서드로 __init__() 이라는 메서드가 있다. 
        - 이것을 흔히 클래스 initializer라고 부른다. 
            * Python에서 두개의 밑줄(__)로 시작하고 두개의 밑줄로 끝나는 레이블은 보통 특별한 의미를 갖는다. 
        - initializer는 클래스로 부터 객체를 만들 때, 인스턴스 변수를 초기화 하거나 객체의 초기상태를 만들기 위한 문장들을 실행하는 곳이다. 
            *Python의 initializer는 JAVA의 Constructor와 약간 다르다. Python에서 클래스 생성자는 실제 runtime 엔진 내부에서 실행되는데,
            이 생성자(Constructor) 실행 도중 클래스 안에 initializer가 있는지 체크하여 만약 있으면 initializer를 호출하여 객체의 변수 등을 초기화 한다. 
    """

    def __init__(self, width, height):
        # self.* : 인스턴스 변수
        self.width = width
        self.height = height
        Rectangle.count += 1


# 인스턴스 메서드
def calcArea(self):
    area = self.width * self.height
    return area


"""
Python은 다른 언어에서 사용하는 접근제한자를 갖지 않는다. (public, protected, private등)
Python 클래스는 기본적으로 모든 멤버가 public이라고 할 수 있다. 

만약 특정 변수명이나 메서드를 privateㅇ로 만들어야 한다면 두개의 밑줄 (__)을 이름 앞에 붙이면된다. 
"""

'''
** Python 에서는 @ 를 어노테이션이라고하지않고 데코레이터라고 부른다. decorator 

정적메서드와 클래스 메서드
* 인스턴스 메서드가 객체의 인스턴스 필드를 self를 통해 엑세스 할 수 있는 반면에, 

정적 메서드는 self 파라미터를 갖지 않고 인스턴스 변수에 접근할 수 없다.
    따라서, 정적 메서드는 보통 객체 필드와 독립적이지만, 로직상 클래스내에 포함되는 메서드에 사용된다. 
    정적 메서드는 메서드 앞에 @staticmethod라고 표시한다.
    
클래스 메서드는 메서드 앞에 @classmethod라고 표시한다. 
    클래스 메서드는 정적 메서드와 비슷한데, 객체 인스턴스를 의미하는 self 대신, cls라는 클래스를 의미하는 파라미터를 전달 받는다. 
    정적 메서드는 이런 cls 파라미터를 전달받지 않는다. 
    클래스 메서드는 이렇게 전달받은 cls 파라미터를 통해 캘래스 변수 등을 엑세스 할 수 잇다.
    
일반적으로, 인스턴스 데이터를 접근할 필요가 없는 경우 클래스 메서드나 정적 메서드를 사용하는데, 
이때 보통 클래스 변수를 접근할 필요가 있을 때는 클래스 메서드를,
이를 엑세스할 필요가 없을 때는 정적 메서드를 사용한다. 

'''


# 정적 메서드
@staticmethod
def isSquare(rectWidth, rectHeight):
    return rectWidth == rectHeight


# 클래스 메서드
@classmethod
def printCount(cls):
    print(cls.count)
