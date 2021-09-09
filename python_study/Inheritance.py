'''
Inheritance

- 사용방법 : 자식클래스(부모클래스) ex) Dog (Animal)
- Python은 다중상속 받을 수 있다.
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("move")

    def speak(self):
        pass

class Dog (Animal) :
    def speak(self):
        print ("bark")

class Duck (Animal):
    def speak(self):
        print("quack")


dog = Dog ("doggy")
n = dog.name
dog.move()
dog.speak()
print(n)

'''
Polymorphism

- 다형성도 지원함 
'''

animals = [Dog('doggy'), Duck ('dukky')]
for animal in animals:
    print(animal.name)
    animal.speak()
