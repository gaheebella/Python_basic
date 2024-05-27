str = input("입력 문자열: ")

nums = [int(x) for x in str.split() if x.isdigit()]

#문자열을 split()으로 쪼개고 리스트에 넣은 다음, 리스트 안의 각각의 문자열을 isdigit()으로 숫자일때만 정수형으로 추출

print("추출된 숫자: ", nums)
