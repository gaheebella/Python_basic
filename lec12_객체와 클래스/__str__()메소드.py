#__str__()메소드는 객체를 print()로 출력할 때 자동적으로 호출됨.

class Counter:
    def __init__(self, count):
        self.count = count

    def increment(self):
        self.count += 1

    def __str__(self): #객체의 값을 출력함
        msg = "카운트 값: " + str(self.count)
        return msg

a = Counter(100)
print(a) #자동적으로 str메소드가 호출됨
