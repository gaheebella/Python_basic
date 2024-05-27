#머리 글자어 만들기
phrase = input()

acronym = " "

for word in phrase.upper().split(): #다 대문자로 만들어서 공백 기준으로 자른다
    acronym += word[0]

print(acronym)