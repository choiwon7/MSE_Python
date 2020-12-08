date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_price = dict(zip(date,close_price)) #키와 값의 형태로 묶어주어야하기때문에, dict를 이용하여 묶어준다.
                                          #이후 zip(같은 길이가 묶어주는 내장함수)를 이용하여 date와 close_price를 묶어준다.
                                          #문제에서 print(close_price)했기때문에 close_price를 그대로 변수 지정한다.
print(close_price)                        #close_price를 출력한다.