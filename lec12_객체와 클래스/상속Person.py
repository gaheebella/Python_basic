#상속-> 상속을 그대로 받고 기존의 메소드 내용을 바꿀 수 있음

class Person: #부모클래스
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isStudent(self):
        return False


class Student(Person): #자식클래스_ Person클래스를 상속받음
    def __init__(self, name, gpa): #자식클래스의 생성자에선 부모클래스의 생성자도 호출해주어야 함
        super().__init__(name) #부모클래스의 생성자가 호출됨
        self.gpa = gpa #자식클래스는 부모클래스의 변수에 추가로 필요한 변수들 정의 가능
    def isStudent(self): #부모클래스의 메소드를 변경해서 사용 가능 = 메소드 오버라이딩
        return True

a = Person("Yang")
b = Student("Kim", 4.5)
print(a.getName(), a.isStudent(), a.name)
print(b.getName(), b.isStudent(), b.gpa)