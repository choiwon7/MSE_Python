class 부모:            #클래스 부모 정의
  def __init__(self): #생성자 정의
    print("부모생성")    

class 자식(부모):       #클래스 자식 정의
  def __init__(self): #생성자 정의
    print("자식생성")   
    super().__init__()#부모클래스에 접근 할 수있음 , 그후 부모클래스의 생성자를 호출.
                      #자식에 있는 self가 부모 self로 알아서 전달이 되기때문에 self적어줄 필요 없음.
                      #super: 부모 클래스의 함수를 호출한다.
나 = 자식()  #자식 클래스 객체 생성 ---> 생성자가 있으니 생성자를 호출한다. ----->자식클래스의 생성자가 먼저 탐색된다.-->자식생성먼저 프린트된다.

#결과 : "자식생성"이 프린트되고 , 부모클래스를 호출했으니(super) "부모생성"이 프린트된다.