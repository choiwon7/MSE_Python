a=['intra.h','intra.c','define.h','run.py']
for i in a:
    if i.endswith(('.h','c')):  #endswith : 특정문자로 끝나는지 여부를 알려줌
                                #startswith : 특정문자로 시작하는지 알려줌
                                #'.h'나'.c'로 끝난다면 
        print(i)                #i값을 출력해라.
        
        