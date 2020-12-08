data = [2,4,3,1,5,10]
a = sorted(data)  #sorted 이용하여 숫자를 크기가 낮은것부터 정렬해줌. ( 방법1)
print(a)

data = [2,4,3,1,5,10]
data.sort(reverse = False) #작은 순서부터 정렬시켜라.(방법2)
print(data)

data = [2,4,3,1,5,10]
data.sort()     #data의 요소를 작은 순서부터 정렬시켜라(sort 이용)
print(data) 