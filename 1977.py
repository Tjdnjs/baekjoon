# M, N 이 주어질 때 M 이상, N 이하 중 완전제곱수
# 합\n 최솟값 출력

import sys
import math
input = sys.stdin.readline

M = int(input())
N = int(input())

m = math.ceil(math.sqrt(M))
n = math.trunc(math.sqrt(N))
square_num = []

for i in range(m,n+1):
    if i*i<=N:
        square_num.append(i*i)

if len(square_num)==0:
    print(-1)
else:
    print(sum(square_num))
    print(min(square_num))