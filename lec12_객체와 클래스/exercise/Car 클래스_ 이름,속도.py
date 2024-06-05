class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get(self):
        print(f"{self.name}의 현재 속도는 {self.speed}입니다.")

a = Car("아우디", 0)
b = Car("벤츠", 30)
a.get()
b.get()

