#패스워드 조건: 1.최소 8글자 2.적어도 하나의 대문자 3.적어도 하나의 숫자
import re

def check():
    while True:
        psw = input("패스워드를 입력하시오: ")
        if (len(psw) < 8):
            print("최소 8글자이어야 함")
        elif (re.search('[A-Z]',psw)) is None:
            print("적어도 하나의 대문자 가짐")
        elif (re.search('[0-9]',psw)) is None:
            print("적어도 하나의 숫자 가짐")
        else:
            print("적합한 패스워드")
            break

check()