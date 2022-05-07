# N(1-10) 명의 사람 한 줄로
# 자기보다 큰 사람이 왼쪽에 몇 명 있었는 지만 기억
# 첫 줄 : N, 둘째 줄 : 키가 1인 사람부터 차례로 기억하는 명 수
# N-i>=i번째 수 >=0, i는 0부터 시작 - 순서대로 키 출력

import sys
input = sys.stdin.readline

N = int(input())
height = list(map(int,input().split()))
height.reverse()
result = []

for i in range(N):
    result.insert(height[i],N)
    N-=1

for i in result:
    print(i, end=' ')