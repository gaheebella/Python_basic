#Private 인스턴스 변수-> 클래스 내부에서만 접근 가능
class Student:
    def __init__(self, name=None, age=0):
        self.__name = name
        self.__age = age

#인스턴스 반환_ 접근자get, 설정자set
    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def setName(self, name):
        self.__name = name

p = Student("Yang", 24)
print(p.getName())
print(p.getAge())

p.setAge(22)
p.setName("kim")
print(p.getName())
print(p.getAge())

