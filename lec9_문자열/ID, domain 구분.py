address = input("이메일 주소를 입력하시오: ")

(ID, domain) = address.split("@")

print(address)
print("아이디: ", ID)
print("도메인: ", domain)