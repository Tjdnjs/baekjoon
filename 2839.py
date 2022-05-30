# N 킬로그램, 3,5 담을 수 있는 봉지
# 봉지의 최소 개수

N = int(input())
cnt=0

while N%5!=0 and N>2:
    N-=3
    cnt+=1

if N%5==0 or N%3==0:
    cnt+=N/5
    print(int(cnt))
else:
    print(-1)
