# 양의 정수 X의 각 자리가 등차수열을 이룸, 그 수 : 한수 / 1<= <=N 인 한수의 개수

def hansu(N):
    if N < 100:
        return True
    x = N // 100
    y = N // 10 % 10
    z = N % 10
    return x+z == 2*y

N = int(input())
cnt = 0
for i in range(1, N+1):
    if hansu(i):
        cnt += 1

print(cnt)