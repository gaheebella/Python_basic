s1 = input("첫 번째 문자열: ")
s2 = input("두 번째 문자열: ")

#set로 만들어서 교집합연산 > 그걸 다시 리스트로 만든 뒤> 하나씩 출력

same = list(set(s1) & set(s2))

print("\n공통된 글자: ", end='')

for i in same:
    print(i,",", end='')