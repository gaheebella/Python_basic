import random

s = "0123456789" #대상 문자열
psw_len = 4 #패스워드 길이

#random.sample(sequence,k)
#sequence: 리스트,집합,range(숫자) 등 random의 범위
#k: 반환될 리스트의 크기
psw = ''.join(random.sample(s, psw_len))

print(psw)