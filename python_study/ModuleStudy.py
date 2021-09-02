"""
Module
    - Module은 Python 코드를 논리적으로 묶어서 관리하고 사용할 수 있도록 하는 것.
    - 보통 하나의 파이썬 .py파일이 하나의 Module이 된다.
    - Module 안에는 Function, Class, Variation 등이 정의될 수있고, 실행 코드를 포함 할 수 도 있다.

    - Python은 기본적으로 많은 표준 라이브러리 Module들을 제공하고 있다.
    - 3rd Party에서도 많은 Module들을 제공하고 있다.
    - 이를 사용하기 위해서는 Module들을 import해서 사용하면 된다.
    - import module1[, module2[, .... , moduleN] 과 같은 형식으로 여러개 복수의 모듈을 불러들일 수있다.

"""

# math module 활용

import math

n = math.factorial(5)
print(n)

"""
하나의 Module 안에는 여러 함수 들이 존재할 수 있다. 
이 중 하나의 함수만을 불러 사용하기 위해서는 from 모듈명 import 함수명 을 사용하면된다.
    -> 이렇게 되었을 시, "모둘명.함수명" 의 형태로 불러오지 않고 직접 "함수명"으로 기능 사용이 가능하다. 
"""
from math import factorial

n = factorial(6)
print(n)

"""
하나의 모듈 안에 있는 여러 함수를 사용하기 위해 from ... import(함수1, 함수2)와 같이 나열할 수 있다. 
모든 함수를 불러사용하기 위해서 *를 사용할 수 도 있다.
"""

from math import (factorial, acos)

n = factorial(4) + acos(1)

from math import *

n = sqrt(5) + fabs(-12.5)

"""
함수에 Alias주기
    - 함수의 이름이 길거나 어떤 필요에 의해 Alias를 주고 싶은 경우가 있는데, 이 때는 "함수명 as Alias"와 같은 표현을 사용할 수 있다.
"""

from math import factorial as f  # Alias주기

n = f(5) / f(3)
print(n)

"""
Module의 위치
    - Python에서 Module을 import하면 그 module을 찾기 위해 다음의 경로를 순서대로 검색한다.
        1. 현재 디렉토리
        2. 환경변수 PythonPath에 지정된 경로
        3. Python이 설치된 경로 및 그 밑의 라이브러리 경로
    이러한 경로들은 모두 취합되어 시스템 경로인 sys.path에 리스트 형태로 저장된다. 
"""

import sys

print(sys.path)

"""
Module 불러오기 실습
"""

from mylib import *

i = add(10, 20)
i = substract(20, 5)

"""
Python 모듈 .py파일은 import하여 사용할 수 있을 뿐 아니라, 해당 모듈 파일 안에 있는 스크립트 전체를 바로 실행할 수도 있다. 
Python 에서 하나의 module을 import하여 사용할 때와 스크립트 전체를 실행할 때를 동시에 지원하기 위해 관행적으로 모듈 안에서 __name__을 체크한다.
Python에서 module을 import해서 사용할 경우, 그 모듈 안의 __name__은 해당 모듈의 이름이 된다. 
모듈을 스크립트로 실행할 경우 그 모듈안의 __name__은 "__main__"이 된다. 
예를 들어, run.py라는 모듈을 import하여 사용할 경우 __name__은 run.py가 되고, 
"python3.8 run.py"와 같이 인터프리터로 스크립트를 바로 실행할 때 __name__은 __main__이 된다.
"""

# import sys
#
#
# def openurl(url):
#     print(url)
#
#
# if __name__ == '__main__':
#     openurl(sys.argv[1])
