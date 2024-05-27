import re

phone_num = input()
pattern = r'010-\d\d\d\d-\d\d\d\d' #정규식

found = re.search(pattern, phone_num)
print("발견된 핸드폰 번호: " + found.group())