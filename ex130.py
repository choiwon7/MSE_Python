import requests  #requests 모듈을 사용하기 위해서import로 선언해준후, request:웹에대해 요청을해서 데이터를 가져온다.
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data'] #get을 이용해서 소스를 가져온다.

high = float(btc['max_price']) #btc['max_price']의 type이 str이기때문에 실수 자료형인 float로 변경
low = float(btc['min_price'])  #btc['min_price']의 type이 str이기때문에 실수 자료형인 float로 변경
diff = high - low #변동폭
open = float(btc['opening_price'])   #초기값
if (open + diff) > high:  #비교연산자(>)가 계산(+)보다 우선순위이기 때문에, 괄호를 쳐서 먼저 계산해주고 비교를 해야한다.
    print('상승장')
else :
    print('하락장')
    