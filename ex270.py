class Stock:
    pass    
#Stock 안에 비어있는 공간생성
    
#__init__는 클래스를 초기화 하는 함수---->클래스를 생성할때 자동으로 호출되는 함수(self는 init와 항상 같이사용)
#객체가 생성될때 값을 입력받아야함. 



class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        
        #__init__는 클래스를 초기화 하는 함수---->클래스를 생성할때 자동으로 호출되는 함수(self는 init와 항상 같이사용)
       #객체가 생성될때 값을 입력받아야함. 
        self.name = name  #self라는 공간안에 name을 만들고 함수 인자 name가 가리키는 변수를 가리켜라.
        self.code = code  #self라는 공간안에 code을 만들고 함수 인자 code가 가리키는 변수를 가리켜라.
        self.per = per    #self라는 공간안에 per 을 만들고 함수 인자 per이 가리키는 변수를 가리켜라.
        self.pbr = pbr    #self라는 공간안에 pbr을 만들고 함수 인자 pbr이 가리키는 변수를 가리켜라.
        self.배당수익률 = 배당수익률  #self라는 공간안에 배당수익률을 만들고 함수 인자 배당수익률이 가리키는 변수를 가리켜라.

    def set_name(self, name): #set : 어떤객체에 어떤값을 선택할건지
                              #self : 어떤 객체에 있는 이름을 바꾼건지 알려줄 필요가 있기때문에
        self.name = name      #name 이라는 변수가 새로 왔으므로 새로 가리킴.

    def set_code(self, code): 
        self.code = code

    def get_name(self):      #get 어느객체로 가져갈건지 
        return self.name     #self가 가리키는 공간의 이름을 return해준다.

    def get_code(self):      #get 어느객체로 가져갈건지 
        return self.code     #self가 가리키는 공간의 코드를 return해준다. 
        
    def set_per(self, per):  
        self.per = per       #self가 가리키는 per을 새로운 per로 바꿔준다.

    def set_pbr(self, pbr):
        self.pbr = pbr       #self가 가리키는 pbr을 새로운 pbr로 바꿔준다.

    def set_dividend(self, dividend):
        self.dividend = dividend  #self가 가리키는 dividend을 새로운 dividend로 바꿔준다.
        
        
종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83) 
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)      #list에 넣기위해 append 내장함수 이용.
종목.append(현대차)     #list에 넣기위해 append 내장함수 이용.
종목.append(LG전자)    #list에 넣기위해 append 내장함수 이용.

for i in 종목:
    print(i.code, i.per)        # i-> Stock 클래스의 객체를 바인딩하기 때문   
        