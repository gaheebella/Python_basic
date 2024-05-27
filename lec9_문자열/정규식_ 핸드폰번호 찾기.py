import re #정규식 함수 모듈

phone_num = input()
pattern = r'010-\d\d\d\d-\d\d\d\d' #정규식
# r:원시문자열_백슬래시를 이스케이프문자가 아닌 문자열의 일부로 취급

found = re.search(pattern, phone_num)
print("발견된 핸드폰 번호: " + found.group())
#정규식 패턴 발견시 match객체의 group()호출-> 일치된 문자열 반환