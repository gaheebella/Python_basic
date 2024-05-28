# 아스키코드 A-Z: 65~90, a-z: 97~122 -> 26개씩
# 문자열 str을 각 문자가 알파벳인 경우에만 move만큼 이동하여 암호화

def sol(s, move):
    s = list(s) #입력받은 문자열을 리스트로 만들어서 하나씩 접근. s는 리스트

    for i in range(len(s)):
        if (s[i].isupper()): #대문자라면
            s[i] = chr((ord(s[i]) - ord('A') + move) % 26 + ord('A'))
        elif (s[i].islower()): #소문자라면
            s[i] = chr((ord(s[i]) - ord('a') + move) % 26 + ord('a'))

    return "".join(s) #이동된 문자들을 모두 합침

# ord(s[i]) - ord('A') : 문자 s[i]가 A로부터 얼마나 떨어져 있는지
# move만큼 이동한 뒤에 알파벳의 범위를 벗어나지 않도록 %26 연산 수행
# 다시 'A'부터 시작하기 위해 +ord('A')

str = input("입력 문자열 = ") #암호화할 문자열
move = int(input("이동값 = ")) #몇 칸 이동할지

print("출력 문자열 =", sol(str, 3))