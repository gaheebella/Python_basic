class Dog:
    count = 0

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        Dog.count += 1
        self.number = Dog.count

    def show(self):
        print(f'강아지 #{self.number} = "{self.name}", {self.age}, "{self.color}"')

a = Dog("Molly", 10, "brown")
b = Dog("Daisy", 6, "black")
c = Dog("Bella", 7, "white")
a.show()
b.show()
c.show()
print(f"현재까지 생성된 강아지의 수 = {c.number}")