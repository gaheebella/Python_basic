class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

a = Car("blue", 10000)
b = Car("red", 20000)

print(f"{a.color} 자동차의 주행거리는 {a.mileage}입니다.")
print(f"{b.color} 자동차의 주행거리는 {b.mileage}입니다.")