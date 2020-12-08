import numpy                            #numpy 모듈을 이용하기위해 import 사용 (range는 정수값만 증가가능. --->사용불가)
for i in numpy.arange(0, 5, 0.1):       #arragne : 소수점단위로도 증가 가능함. 
    print(i)                            #0 , 0.1, 0.2 '''''5까지 0.1씩 증가한다.