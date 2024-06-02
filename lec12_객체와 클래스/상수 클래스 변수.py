class Monster:
    #클래스 변수
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERYSTRONG = 30

    def __init__(self):
        self.__health = Monster.NORMAL

    def eat(self):
        self.__health = Monster.STRONG

    def attack(self):
        self.__health = Monster.WEAK

    def getHealth(self): #private 인스턴스변수인 health 접근자
        return self.__health


c = Monster()
c.eat()
print(c.getHealth()) #private변수는 getter함수를 통해 값 접근
c.attack()
print(c.getHealth())