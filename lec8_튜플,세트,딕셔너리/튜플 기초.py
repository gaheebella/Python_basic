fruits = ()
fruits = ("apple", "banana", "grape")
result = fruits[1] #요소 접근 (수정 불가)


#튜플에 데이터 하나만 저장시 쉼표 필요
single_tuple = ("apple",)


#튜플을 바꾸고 싶다면? 리스트로 바꾸고 수정한 뒤 다시 튜플로
myTuple = (1, 2, 3, 4) #수정 불가
myList = list(myTuple)
myList.append(5)
myTuple = tuple(myList)


#튜플끼리 or 튜플+리스트 합치기 가능
fruits += ("pear", "kiwi")
numbers = [10, 20, 30]
numbers += (40, 50)


#enumerate() : 인덱스(key) & 데이터(value) 함께 출력
for index, value in enumerate(fruits):
    print(index, value)
