import random

print("**로또 추첨을 시작합니다.**")

list = []

for i in range(5):
    num = random.randint(1, 45)
    list.append(num)

print("추첨된 로또 번호 ==> ", list)