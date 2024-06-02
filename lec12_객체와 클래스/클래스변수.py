# 클래스 변수 =>모든 객체를 통틀어서 하나만 생성되고 모든 객체가 공유하는 변수

class Television:
    serialNumber = 0 #클래스 변수

    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
        Television.serialNumber += 1 #클래스 변수 값 1 증가
        self.number = Television.serialNumber #클래스 변수값을 객체의 넘버로 함

    def show(self):
        print(self.channel, self.volume, self.on, self.number)

myTV = Television(10,3,True)
myTV.show()