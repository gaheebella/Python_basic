str = "Hello World!"

str_dic = {}

strList = list(str)
print(strList)

for chr in strList:
    if chr in str_dic:
        str_dic[chr] += 1
    else:
        str_dic[chr] = 1

print("입력 문자열 = " + str)
print("실행 결과 = ", str_dic)
