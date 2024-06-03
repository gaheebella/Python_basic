import math

class Circle:
    def __init__(self, radius = 0):
        self.radius = radius

    def getArea(self):
        area = math.pi * self.radius * self.radius
        return area

    def getPerimeter(self):
        return 2 * math.pi * self.radius

    def __gt__(self, other):
        return self.getArea() > other.getArea()

c1 = Circle(10)
c2 = Circle(20)
print("원 #1 = 반지름", c1.radius)
print("원 #2 = 반지름", c2.radius)

if c1 > c2:
    print("원 #1 > 원 #2 는 True 입니다.")
else:
    print("원 #1 > 원 #2 는 False 입니다")



