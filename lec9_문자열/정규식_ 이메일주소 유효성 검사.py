import re

pattern = r'^[\w]+@[\w]+\.[A-Za-z]{2,4}$' #이메일 주소 정규식

def checkEmail(emailAddress):
    if (re.search(pattern, emailAddress)):
        print(f"{emailAddress}는 유효한 이메일 주소")
    else:
        print(f"{emailAddress}는 유효하지 않은 이메일 주소")


email = input()
checkEmail(email)
