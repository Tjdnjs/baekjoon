# M 이상 N 이하 소수 모두 출력

M, N = map(int, input().split())
isPrime = [True]*(N+1)
isPrime[0] = False
isPrime[1] = False

for i in range(2,int(N**0.5)+1):
    if isPrime[i]:
        for j in range(i+i, N+1, i):
            isPrime[j]=False

for i in range(M,N+1):
    if isPrime[i]:
        print(i)