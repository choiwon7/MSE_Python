def message1():      #함수정의 ---->함수이름을 message1
    print("A")       #print 'A'를해라

def message2():      #함수정의 ---->함수이름을 message2
    print("B")       #print 'B'를해라

def message3():      #함수정의 ---->함수이름을 message3
    for i in range (3) : #반복문을 3번돈다.
        message2()   #message2를 출력하고
        print("C")   #C를 출력한다.  --->3번반복후
    message1()       #for문이 끝났으니까 message1를 출력함 
                     #B,C,B,C,B,C,A
                     
                     
message3()         #message3을 실행하겠다.