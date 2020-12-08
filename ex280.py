import random  #랜덤모듈.


class Account:        #클래스이름
    # class variable
    account_count = 0

    def __init__(self, name, balance):  #생성자에서 입력받는값 : 이름 , 잔고
        self.deposit_count = 0      
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name        #입력받은 이름을 self가 가리키는 공간에 name라는 이름을 만들고 저장
        self.balance = balance  #입력받은 이름을 self가 가리키는 공간에 balance라는 이름을 만들고 저장
        self.bank = "SC은행"     #은행이름 sc제일은행

        # 3-2-6
        num1 = random.randint(0, 999)  #*randint: 특정 범위의 정수를 랜덤하게 발생시키는 함수(3자리 랜덤으로 나옴)
        num2 = random.randint(0, 99)   #2자리 랜덤으로 나옴
        num3 = random.randint(0, 999999) #6자리 랜덤으로 나옴

        num1 = str(num1).zfill(3)  # 숫자를 문자로 바꾼담에 00x값으로 변경  
        num2 = str(num2).zfill(2)  # 숫자를 문자로 바꾼담에 0x값으로 변경  
        num3 = str(num3).zfill(6)  # 숫자를 문자로 바꾼담에 00000x값으로 변경  
        self.account_number = num1 + '-' + num2 + '-' + num3  # 문자연결함. --->계좌번호 생성
        Account.account_count += 1
            
            #zfill 원하는 자리수 만들어주는것 앞에 0을채움.
            
            
    @classmethod   #----->객체에 접근할 필요 없는애들      
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount):  #얼마를 입금할건지 amount받는다
        if amount >= 1:         #입금액이 1원이상이면 
            self.deposit_log.append(amount) #입금이 한번 일어날때마다 리스트 저장.
            self.balance += amount #잔고에다가 입금액을 더해라. 그리고 그값을 balance에 저장해라.

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount): #얼마를 출금할건지 amount받는다
        if self.balance > amount: #잔고에서 출금요청액 빼기 ----->마이너스 통장아님.(만약에 잔고가 출금액(amount)이상이면)
            self.withdraw_log.append(amount) #출금이 한번 일어날때마다 출금액 저장.
            self.balance -= amount #잔고에서 출금액을 빼라 그리고 그값을 balance에 저장해라.

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):
        for amount in self.withdraw_log: 
            print(amount)      #출금액 출력

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)      #입금액 출략


k = Account("Kim", 1000)  #1000입금.
k.deposit(100)  #100원예금
k.deposit(200)  #200원예금
k.deposit(300)  #300원예금
k.deposit_history() # 함수 호출.

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()

        


        