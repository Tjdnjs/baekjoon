# 배열 크기 10, N=3
# 테스트케이스의 수 -> N번째 큰 값 출력

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    print(A[2])