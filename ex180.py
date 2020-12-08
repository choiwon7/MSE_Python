volatility = []
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
for i in range(len(low_prices)) :  #range와 len를 이용해서 low_prices와 high_prices의 길이만큼 숫자를 만든다.
    volatility.append(high_prices[i] - low_prices[i]) #volatility에 리스트 형태로 넣어주기위해 
                                                      #list 내장함수인 append를 이용해서 변동폭을 volatility에 리스트 형태로 저장한다.

print(volatility) #volatility값을 출력한다.                                                                    