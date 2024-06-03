import math

class Circle:
    def __init__(self, radius = 0):
        self.radius = radius

    def getArea(self):
        return math.pi * (self.radius ** 2)

    def getPerimeter(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius  # __eq__()메소드가 정의된 객체는 ==연산자를 이용해 비교가능

c1 = Circle(10)
c2 = Circle(10)

if c1 == c2:
    print("c1과 c2의 원의 반지름이 동일함")

print("c1원의 면적 = ", c1.getArea())
print("c2원의 둘레 = ", c2.getPerimeter())