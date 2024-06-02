class Counter:
    def __init__(self, initValue):
        self.count = initValue

    def increment(self):
        self.count += 1

a = Counter(0) #0으로 초기화
b = Counter(100) #100으로 초기화

print("메소드 전 카운터 값 = ", a.count)
a.increment()
print("메소드 후 카운터 값 = ", a.count)

print("메소드 전 카운터 값 = ", b.count)
b.increment()
print("메소드 후 카운터 값 = ", b.count)