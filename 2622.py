# 같은 길이 성냥개비 여러 개
# 삼각형
# 여러 개의 성냥개비를 이어서 만듦 - 서로 다른 삼각형 개수?

N = int(input())
cnt = 0

for x in range(1,N):
    if 2*x < N <= 3*x:
        cnt += x-(N-x-1)//2

print(cnt)