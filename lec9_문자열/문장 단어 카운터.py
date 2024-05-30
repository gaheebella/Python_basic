text_data = "Create the highest, grandest vision possible for your life, because you become what you believe"

word_dic = {} #단어 딕셔너리_ 단어word(key값): 출현횟수count(value값)

for word in text_data.split(): #text_data를 공백기준으로 잘라서 한 단어 word가 key값
    if word in word_dic: #딕셔너리 안에 word가 이미 있으면
        word_dic[word] += 1 #해당 word(key값)의 count(value값)를 1 증가
    else:
        word_dic[word] = 1 #없으면 1로 초기화시키기

for word, count in sorted(word_dic.items()): #key,value값 출력_딕셔너리는 items이용
    print(word, "의 등장횟수: ", count)
