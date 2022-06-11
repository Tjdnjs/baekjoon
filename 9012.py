# VPS : 괄호 문자열 YES or NO
# 표준 입력 사용, T개의 테스트데이터(길이 2~50)
# 표준 출력 사용, 한 줄에 하나씩 출력

T = int(input())

for _ in range(T):
    string = input()
    PS = list(string)
    cnt=0
    for i in PS:
        if i=='(':
            cnt+=1
        elif i==')':
            cnt-=1 
        if cnt<0:
            print('NO')
            break      
    if cnt==0:  
        print('YES')
    if cnt>0:
        print('NO')


