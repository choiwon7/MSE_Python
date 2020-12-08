per = ["10.31", "", "8.00"]

for i in per:        #per을 i에 대입한다.
    try:             # 실행코드
        print(float(i))  #----->per에 ""가 있어서 실수로 변환이 안되어 오류가 발생할것임.
    except:          #예외가 발생할경우 
        print(0)     #0으로 표현해라
    else:            #예외가 발생하지않으면
        print("clean data") #clean data를 실행해라
    finally:         #예외가 발생하던말던
        print("변환 완료") #변환완료 출력하기.
        
       #10.31 clean data 변환완료 , 0 변환완료 , 8.00 clean data 변환완료 이렇게 됌.