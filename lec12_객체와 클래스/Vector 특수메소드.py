class Vector2D:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __subtract__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __equal__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    #문자열 포매팅-> " " 안에 %기호를 사용하고, 맨 뒤에 %로 그 자리에 들어갈 값을 입력

u = Vector2D(0, 1)
v = Vector2D(1, 0)
w = Vector2D(1, 1)
a = u + v
print(u, "+", v, "=", a)

