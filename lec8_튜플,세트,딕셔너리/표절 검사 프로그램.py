#문자열 비교-> 둘 다 모두 대문자(or 소문자)로 만들어서 비교

s1 = input("문자열 1 : ")
s2 = input("문자열 2 : ")

s1 = s1.lower()
s2 = s2.lower()

#문자열을 공백 기준으로 한 단어씩 분리해서 리스트에 넣기
list1 = s1.split(" ")
list2 = s2.split(" ")

total = len(list1)
same = len(list(set(list1) & set(list2))) #공통된 부분을 세트의 교집합 이용

print("표절률 = ", (same/total) * 100)