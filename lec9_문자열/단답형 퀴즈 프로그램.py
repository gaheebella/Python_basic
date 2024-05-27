#단답형문제 출제&채점_ 딕셔너리 이용

Question = {"CPU는 무엇의 약자인가?":"Central Processing Unit", "제일 쉬운 프로그래밍 언어는?":"python"}
# key : Question[key]

for key in Question:
    print(key)
    Answer = input("답안을 작성하시오(또는 quit): ")
    if (Answer.lower() == Question[key].lower()):  #문자열 비교하려면 대소문자 하나로 통일해서
        print("정답입니다.")
    elif (Answer == "quit"):
        break
    else:
        print("오답입니다.")