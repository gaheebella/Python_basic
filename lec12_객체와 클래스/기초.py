# Counter 클래스 정의
# 모든 메소드의 첫 번째 매개변수는 현재 객체를 가리키는 self 변수 포함
# 생성자의 매개변수 갯수는 객체의 매개변수 갯수와 같아야 함

class Counter:
    def __init__(self): #생성자_객체 초기화
        self.count = 0 #인스턴스변수 count -> 0으로 초기화

    def increment(self):
        self.count += 1

#인스턴스 변수 = 생성자 안에서 선언, 클래스 안에 선언된 변수, 앞에 self.이 붙음
#지역변수 = 메소드 안에서 선언, 메소드 안에서만 사용 가능
#전역변수 = 메소드 외부에서 선언

a = Counter() #객체a 생성_ '클래스이름()'
a.increment() #객체 메소드 호출
print("카운터의 값 = ", a.count) #객체a의 인스턴스 변수count에 접근
