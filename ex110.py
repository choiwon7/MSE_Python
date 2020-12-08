if True :          #True이기 때문에 맨 아래에 있는 else는 볼 필요없음.
    if False:      #만약에 False라면
        print("1") #1을 출력해라
        print("2") #2를 출력해라     
    else:          #그렇지 않다면
        print("3") #3을 출력해라.
        
        ###여기서 True이기 때문에 두번째 if 구문에 걸려있는 False도 볼 필요없음.따라서 두번째 if문에 걸려있는 else의 3이 출력된다.
else :
    print("4") #첫번째 if가 사실이 아니라면 4를 출력해라.
print("5") 

# 3,5 이다. 조건이 참이고 if를 보면 if fasle와 else가 있는데 참이기때문에 else를 봐야한다.
#따라서 3이 출력되고, print(5)를 했기때문에 5가 출력된다. 출력값 : 3,5