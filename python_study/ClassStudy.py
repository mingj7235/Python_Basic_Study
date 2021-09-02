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

    # 메서드
   def calcArea (self) :
       area = self.width * self.height
       return area

"""
Python은 다른 언어에서 사용하는 접근제한자를 갖지 않는다. (public, protected, private등)
Python 클래스는 기본적으로 모든 멤버가 public이라고 할 수 있다. 

만약 특정 변수명이나 메서드를 privateㅇ로 만들어야 한다면 두개의 밑줄 (__)을 이름 앞에 붙이면된다. 
"""