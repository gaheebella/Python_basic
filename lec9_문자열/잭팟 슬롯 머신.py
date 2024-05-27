list1 = ['ABC', 'ABC', 'ABC']
list2 = ['@@@', 'ABC', 'ABC']

#집합은 중복된건 하나만 나타냄-> 길이=1 이면 집합 안에 모든 문자가 동일하다는 것
def check(list):
    if (len(set(list)) == 1):
        print(list, "-> Jack Pot!!")
    else:
        print(list, "-> Not Jack Pot!!")

check(list1)
check(list2)
