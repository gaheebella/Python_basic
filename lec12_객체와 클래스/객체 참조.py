# 파이썬에서 변수는 실제로 객체를 저장하지 않음. 단지 객체의 메모리 주소를 저장함

class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

    def setChannel(self, channel):
        self.channel = channel

t = Television(10, 20, True) #변수 t는 객체를 저장하는게 아닌, 객체의 참조값만 저장함
print("t의 channel번호 = ", t.channel)
s = t
#객체가 복사되는 것이 아닌, 참조값만 복사되어 변수 s에 저장됨. t와 s가 동일한 객체를 가리킴
#즉, s객체를 수정하면 t객체의 값도 변경됨
print("t의 참조값을 복사하여 s에 저장한 뒤 s의 channel번호 = ", s.channel)
s.channel = 8
print("바꾼 s의 channel번호 = ", s.channel)
print("s를 바꿨을 때 t의 channel번호 = ", t.channel)


#2개의 변수가 동일한 객체를 참조하고 있는지 검사
if s is t:
    print("2개의 변수는 동일한 객체를 참조하고 있음")

if s is not t:
    print("2개의 변수는 다른 객체를 참조하고 있음")