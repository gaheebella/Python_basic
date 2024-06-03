class Account:
    # 클래스 변수
    count = 0
    list1 = []
    list2 = []

    def __init__(self, id, psw):
        self.id = id
        self.psw = psw

        Account.count += 1
        self.number = Account.count

        Account.list1.append(self.id)
        Account.list2.append(self.psw)

    @classmethod
    def show(cls):  # 클래스 메소드
        for i in range(cls.count):
            print(f"사용자 #{i + 1} 아이디 = {cls.list1[i]}, 패스워드 = {cls.list2[i]}")

while True:
    print("====================================")
    print("1. 아이디 등록하기")
    print("2. 로그인 하기")
    print("3. 모든 사용자 아이디 출력")
    print("4. 종료")
    print("====================================")
    num = int(input("번호를 입력하시오: "))

    if num == 1:
        ID = input("아이디 입력: ")
        PSW = input("패스워드 입력: ")
        user = Account(ID, PSW)  # 객체 생성
    elif num == 3:
        Account.show()
    elif num == 4:
        print("종료")
        break
    else:
        print("잘못된 입력. 다시 시도하시오.")
