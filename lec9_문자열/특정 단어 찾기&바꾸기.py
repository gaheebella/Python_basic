s = "파이썬, 편해서 좋지 아니한가"

print("입력 문자열: " + s)


x = s.find("좋지 아니한가") #특정 단어의 해당 인덱스를 찾아서 find()
print("출력 문자열: " + s.replace(s[x:], "좋다")) #다른 단어로 바꾸기 replace()
