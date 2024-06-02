class TV:
    def __init__(self, channel, volume, on): # 3개의 인스턴스변수
        #인스턴스변수 정의
        self.channel = channel
        self.volume = volume
        self.on = on

# 3개의 메소드
    def show(self):
        print(self.channel, self.volume, self.on)

    def setChannel(self, channel):
        self.channel = channel

    def getChannel(self):
        return self.channel


t = TV(11, 63, True) #객체 생성
t.show()
print("현재 채널 = ", t.getChannel())
t.setChannel(22)
print("바꾼 후 채널 = ", t.getChannel())
t.show()


