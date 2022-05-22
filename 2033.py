# 정수 N, 이 수가 10보다 크면 일의 자리, 그 결과가 100보다 크면 다시 10의 자리에서 반ㅇ로림
# N<=99,999,999

import math

N = int(input())
n = str(N)

if N<10:
    print(N)
else:
    for i in range(1,len(n)):
        N = math.floor((N/(10**i)+0.5))*(10**i)
    print(N)