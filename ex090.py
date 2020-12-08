>> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}  #icecream이 딕셔너리형태로 저장되어있음.
>> icecream['누가바'] #에러이유 : 딕셔너리는 keys : values 로 이루어져 있는데 icecream에 keys에는 '누가바'라는 key가 없음.
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    icecream['누가바']
KeyError: '누가바'
