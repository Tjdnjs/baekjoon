# 7331, 733, 73, 7 소수 = 신기한 소수
# N(1<=N<=8) 자리 수 중 신기한 소수 모두 찾기

import math

N = int(input())

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

prime1 = [2,3,5,7]
prime2 = [1,3,5,7,9]

def result(cnt, num):
    if cnt==N:
        print(num)
    for i in prime2:
        x = num*10+i
        if isPrime(x):
            result(cnt+1,x)

for i in prime1:
    result(1,i)
